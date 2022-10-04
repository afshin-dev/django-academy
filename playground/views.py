from django.shortcuts import render

# Create your views here.

def hi(request):
    from django.http import HttpResponse
    return HttpResponse("hi.")