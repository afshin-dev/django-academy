from django.shortcuts import render

# Create your views here.


def hi(request):
    from django.http import HttpResponse
    return HttpResponse("hi.")


def tmpl_hi(request):
    return render(request, "playground/hi.html")
