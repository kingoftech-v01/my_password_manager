from django.shortcuts import render
from .models import Account
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.

@csrf_protect
def add(request):
    if request.method == 'POST':
        account_name = request.POST['account_name']
        site_name = request.POST['site_name']
        site_url = request.POST['site_url']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        phone = request.POST['phone']
        notes = request.POST['notes']

        account = Account(user=request.user, account_name=account_name, site_name=site_name, site_url=site_url, email=email, username=username, password=password, phone=phone, notes=notes)
        account.save()
        return render(request, '')

    return render(request, 'accountmanager/add_account.html')

@login_required
def delete(request):
    return render(request, 'accountmanager/delete.html')

@login_required
def update(request):
    return render(request, 'accountmanager/update.html')

@login_required
def details(request, id):
    account = get_object_or_404(Account, id=id, user=request.user)

    return render(request, 'accountmanager/showaccount.html', {'account': account})
