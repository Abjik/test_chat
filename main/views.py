from django.http import HttpResponse
def home(request):
    return HttpResponse("<h4>Home Page</h4>")

def login(request):
    return HttpResponse("<h4>Login Page</h4>")

def reg(request):
    return HttpResponse("<h4>Registr Page</h4>")