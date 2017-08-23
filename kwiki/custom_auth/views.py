from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
import json
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.


def auth(request):
    return render(request, 'auth_form.html')


def mylogin(request):
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


def mylogout(request):
    logout(request)
    return redirect('/')
