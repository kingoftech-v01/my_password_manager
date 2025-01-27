from django.urls import path
from .views import *

urlpatterns = [
    path('add/', add, name='add account'),
    path('delete/<str:id>', delete, name='delete'),
    path('update/<str:id>', update, name='update'),
    path('details/<str:id>', details, name='details'),
]