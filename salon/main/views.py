from django.shortcuts import render


def index(request):
    return render(request, "main/main.html")

# Create your views here.
