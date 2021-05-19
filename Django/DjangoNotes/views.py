from django.shortcuts import render

# Create your views here.


def base(request):
    return render(request, 'base.html')


def basicsDjango(request):
    return render(request, 'djangobasics.html')


def djangoform(request):
    return render(request, 'djangoform.html')
