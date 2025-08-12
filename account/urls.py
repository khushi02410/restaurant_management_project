from django.urls import path
from .views import *

urlpatterns = [
    path('' , include('home.urls'))
]