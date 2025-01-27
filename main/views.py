from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accountmanager.models import Account
# Create your views here.

@login_required
def index(request):
    accounts = Account.objects.filter(user=request.user)
    return render(request, 'main/dashboard.html', {"accounts": accounts})

def security_analysis(request):
    return render(request, 'main/security_analysis.html')

def parameters(request):
    user = request.user
    return render(request, 'main/profile.html', {'username': user.username, 'email': user.email, 'date_joined': user.date_joined})
