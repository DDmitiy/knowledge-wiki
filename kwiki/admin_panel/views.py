from django.contrib import auth
import json
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    if auth.get_user(request).username:
        return render(request, '', {
            'username': auth.get_user(request).username
        })
    else:
        return render(request, 'auth_form.html')




