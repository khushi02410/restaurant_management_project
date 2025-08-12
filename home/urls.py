from django.urls import path
from .views import home_view
from . import views

urlpatterns = [
    path('',home_view, name='home')
    path('', views_home,name = 'home')
    path('about/', views.about,name='about'),
]