from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index_admin.html')


def auth(request):
    return render(request, 'index.html')
