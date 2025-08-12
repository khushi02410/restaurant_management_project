from django.shortcuts import render

# Create your views here.
path('/orders',OrdersListView.as_view(),name='orders'),