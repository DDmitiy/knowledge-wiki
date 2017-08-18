from django.shortcuts import render, redirect
from django.contrib import auth

# Create your views here.


def home(request):
    return render(request, 'index.html',
                  {'username': auth.get_user(request).username})


def logout(request):
    auth.logout(request)
    return redirect('/')
