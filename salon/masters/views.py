from django.shortcuts import render
from .models import Masters


def masters_list(request):
    all_masters = Masters.objects.all()
    return render(request, 'masters/masters_list.html', {'all_masters': all_masters})
