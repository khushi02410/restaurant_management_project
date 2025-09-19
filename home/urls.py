from django.urls import path
from .views import home_view
from .views import contact_view
from . import views

urlpatterns = [
    path('',home_view, name='home')
    path('', views_home,name = 'home')
    path('about/', views.about,name='about')
    path('contact/', views.contact, name='contact'),
    path ('contact/success', view.contact_success , name='contact_success'),
    path('', views.home , name = 'home'),
    path("feedback/" , feedback_view , name = "feedback"),
    path('menu-categories/' , MenuCategoryListView.as_view() , name='menu-categories'),
    path('menu-items/',MenuItemsByCategoryView.as_view(),name='menu-items-by-category'),

]