import requests
from .user_manager import PasswordlessAuthBackend
from django.contrib.auth import login, logout, authenticate
import simplejson as json
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render, redirect
from .models import User

# Create your views here.


def home(request):
    return render(request, 'index_admin.html')


def auth(request):
    logout(request)
    if request.method == 'POST':
        data = {'status': None}
        username = request.POST.get('username')
        password = request.POST.get('password')
        if requests.post('http://95.213.128.80:8080/auth',
                         data={'login': username, 'password': password}):
            user = User.objects.get_or_create(username=username)
            if user is not False:
                # user.backend = 'django.contrib.auth.backends.ModelBackend'
                user = PasswordlessAuthBackend.authenticate(request, username=username)
                login(request, user)
                # print(str(user))
                data['status'] = 1
        else:
            data['status'] = 0
        data = json.dumps(data)
        return HttpResponse(data, content_type='application/json')
    else:
        return HttpResponseNotAllowed(['POST'])
