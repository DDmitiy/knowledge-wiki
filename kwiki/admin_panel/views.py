from django.contrib.auth import login, logout, authenticate
import json
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    return render(request, 'index_admin.html')


def auth(request):
    if request.method == 'POST':
        data = {'status': None}
        username = request.POST.get('username')
        password = request.POST.get('password')
        # убрал хардкод ауф-бекенда
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            data['status'] = 1
        else:
            data['status'] = 0
        data = json.dumps(data)
        return HttpResponse(data, content_type='application/json')
    else:
        return HttpResponseNotAllowed(['POST'])
