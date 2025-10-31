from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from datetime import datetime
from django.contrib import messages

from rest_framework import status, viewsets, generics, permissions, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

from .models import MenuItem, Contact, MenuCategory, Table
from .serializers import MenuCategorySerializer, MenuItemSerializer, TableSerializer
from utils.validation_utils import is_valid_email
from .forms import ContactForm  # Assuming you have this form

from rest_framework import generics
from .models import Table
from .serializers import TableSerializer

from .models import ContactFormSubmission
from .serializers import ContactFormSubmissionSerializer
from .utils import send_email_notification


# ---------- BASIC DJANGO VIEWS ---------- #

def home(request):
    return render(request, 'home/home.html', {'current_year': datetime.now().year})


def about(request):
    return render(request, 'home/about.html', {'current_year': datetime.now().year})


def contact(request):
    return render(request, 'home/contact.html', {'current_year': datetime.now().year})


def menu(request):
    return render(request, 'home/menu.html', {'current_year': datetime.now().year})


def reservations(request):
    return render(request, 'home/reservations.html', {'current_year': datetime.now().year})


# ---------- MENU VIEW ---------- #

def menu_view(request):
    try:
        items = MenuItem.objects.all()
        return render(request, 'home/menu.html', {'items': items})
    except Exception as e:
        print(f"Error fetching menu items: {e}")
        return HttpResponse("Sorry, we couldn't load the menu right now.")


# ---------- CONTACT FORM VIEW ---------- #

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            subject = f"New Contact Form Submission from {contact.name}"
            message = f"Name: {contact.name}\nEmail: {contact.email}\n\nMessage:\n{contact.message}"
            recipient_list = ["kikieskitchen@gmail.com"]

            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
            messages.success(request, "Message sent successfully!")
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'home/contact.html', {'form': form})


# ---------- SUBSCRIBE VIEW ---------- #

def subscribe_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if not is_valid_email(email):
            return JsonResponse({"error": "Invalid email address"}, status=400)
        return JsonResponse({"message": "Subscription successful!"})
    return JsonResponse({"error": "Invalid request method"}, status=405)


# ---------- DRF API VIEWS ---------- #

class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer


class MenuItemsByCategoryView(APIView):
    def get(self, request, *args, **kwargs):
        category_name = request.query_params.get('category', None)

        if not category_name:
            return Response(
                {"error": "category query parameter is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        items = MenuItem.objects.filter(category__name__iexact=category_name)
        serializer = MenuItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# ---------- PAGINATION + VIEWSET ---------- #

class MenuItemPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class MenuItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    pagination_class = MenuItemPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


# ---------- TABLE VIEWS ---------- #

class TableListView(generics.ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class TableDetailView(generics.RetrieveAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class AvailableTablesAPIView(generics.ListAPIView):
    serializer_class = TableSerializer

    def get_queryset(self):
        # Return only available tables
        return Table.objects.filter(is_available=True)    
    

class ContactFormSubmissionView(generics.CreateAPIView):
    queryset = ContactFormSubmission.objects.all()
    serializer_class = ContactFormSubmissionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()

            send_email_notification(
                recipient_email=contact.email,
                subject="thanks for contacting us "
                message=f"hi{contact.name,\n\nWe recieved you message:\n{contact.message\n\nwe'll get back to you soon!}}"
            )

            return Response(
                {"message": "Your message has been submitted successfully."},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class FeaturedMenuItemView(generics.ListAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        return MenuItem.objects.filter(is_featured=True)
    
