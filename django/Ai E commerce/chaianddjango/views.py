from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello World. You are at chai at dango")
    return render(request, 'website/index.html')


def about(request):
    return HttpResponse("Hello World. You are at about at dango")

def contact(request):
    return HttpResponse("Hello World. You are at raja at dango")