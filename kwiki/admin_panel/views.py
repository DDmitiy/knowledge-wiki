import requests
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import CustomUser

# Create your views here.


def home(request):
    return render(request, 'index_admin.html')


def auth(request):
    if request.method == 'POST':
        data = {'status': None}
        login = request.POST.get('login')
        password = request.POST.get('password')
        if requests.post('http://95.213.128.80:8080/auth',
                         data={'login': login, 'password': password}):
            _, user = CustomUser.objects.get_or_create(username=login)
            data['status'] = str(user)
            code = 200
        else:
            data['status'] = 'Invalid login or password'
            code = 401
        return JsonResponse(data, status=code)
    else:
        return HttpResponseNotAllowed(['POST'])
