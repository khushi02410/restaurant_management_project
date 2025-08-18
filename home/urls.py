from django.urls import path
from .views import home_view
from .views import contact_view
from . import views

urlpatterns = [
    path('',home_view, name='home')
    path('', views_home,name = 'home')
    path('about/', views.about,name='about')
    path('contact/', views.contact, name='contact'),
    path ('contact/', contact_view , name='contact'),
    path('', views.home , name = 'home'),

]