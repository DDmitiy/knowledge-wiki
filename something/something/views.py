from django.shortcuts import render
from django.contrib import auth

# Create your views here.


def home(request):
    return render(request, 'index_admin.html',
                  {'username': auth.get_user(request).username})
