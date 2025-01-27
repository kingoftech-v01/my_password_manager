from django.shortcuts import render

# Create your views here.

def generate_password(request):
    return render(request, 'passwordgenerator/generate_password.html')