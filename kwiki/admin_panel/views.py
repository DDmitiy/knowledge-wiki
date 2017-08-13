import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.


def home(request):
    return render(request, 'index_admin.html')


def auth(request):
    if request.method == 'GET':
        return render(request, 'index_admin.html')
    elif request.method == 'POST':
        try:
            login = CustomUser.objects.get(username=request.POST.get('login'))
        except CustomUser.DoesNotExist:
            error = {'error': 'User not found'}
            # error = {'error': make_password('qwerty')}
        else:
            # if check_password(request.POST.get('password'), user.password):
            if requests.post('http://95.213.128.80:8080/auth', data={'login': login,
                                                                    'password': request.POST.get('password')}):
                return redirect('/')    # auth is success
            else:
                error = {'error': 'Invalid login or password'}

        return render(request, 'index_admin.html', error, status=401)

    else:
        return HttpResponse(status=403)
