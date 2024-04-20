from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name = request.GET.get('name')
    message = request.GET.get('message')
    return HttpResponse(request, f'Hello, {name}! {message}')
# Create your views here.
