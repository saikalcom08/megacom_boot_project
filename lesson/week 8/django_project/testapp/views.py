from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    h = "<h1> Hello world</h1>"
    return HttpResponse(h)

def django_get_page(request):
    return render(request, 'test.html', {})