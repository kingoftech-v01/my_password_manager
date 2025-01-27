from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('security/analysis/', security_analysis, name='security_analysis'),
    path('parameters/', parameters, name='parameters'),
]