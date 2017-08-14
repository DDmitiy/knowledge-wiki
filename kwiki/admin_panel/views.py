import requests
import simplejson as json
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render, redirect
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
            data['status'] = 1
        else:
            data['status'] = 0
        data = json.dumps(data)
        return HttpResponse(data, content_type='application/json')
    else:
        return HttpResponseNotAllowed(['POST'])
