from django.http import HttpResponse
def index(request):
    return HttpResponse("<h4>TEST</h4>")