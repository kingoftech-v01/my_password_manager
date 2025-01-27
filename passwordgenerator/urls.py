from django.urls import path
from .views import *

urlpatterns = [
    path('generate_password/', generate_password, name='generate_password'),
]