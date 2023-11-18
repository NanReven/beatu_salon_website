from django.shortcuts import render, redirect
from .forms import UsersForm


def index(request):
    return render(request, "main/main.html")


def registrate(request):
    error = ''
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'form is not correct'
            return redirect('home_page')
    form = UsersForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/registration.html', data)


def auth(request):
    return render(request, 'main/auth.html')
