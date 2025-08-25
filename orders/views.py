from django.shortcuts import render
from django.conf import render

# Create your views here.
path('/orders',OrdersListView.as_view(),name='orders'),

