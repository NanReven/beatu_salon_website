from django.http import HttpResponse
from django.shortcuts import render


def about_us(request):
    return render(request, 'about/about.html')
