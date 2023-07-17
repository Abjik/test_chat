from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'main/index.html')

def login(request):
    return render(request, 'main/login.html')

def reg(request):
    return render(request, 'main/reg.html')