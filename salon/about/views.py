from django.http import HttpResponse
from django.shortcuts import render


def about_us(request):
    return HttpResponse('<h1>About</h1>')
