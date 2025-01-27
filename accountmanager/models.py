from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    account_name = models.CharField(max_length=100)
    site_name = models.CharField(max_length=100)
    site_url = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()

    def __str__(self):
        return self.account_name
    
    def get_absolute_url(self):
        return f"/accountmanager/{self.id}"
