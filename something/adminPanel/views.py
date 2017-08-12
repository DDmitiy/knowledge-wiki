from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.


def home(request):
    return render(request, 'index_admin.html')


def auth(request):
    password = CustomUser.objects.values().get(username=request.POST.get('login')).get('password')
    if check_password(request.POST.get('password'), password):
        return render(request, 'index.html')
        # return redirect('/')
    return render(request, 'index_admin.html',
                  {'error': 'Invalid login or password'})
    # return redirect('/myadmin/', {'error': 'Invalid login or password'})
