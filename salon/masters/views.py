from django.shortcuts import render, get_object_or_404
from .models import Masters


def masters_list(request):
    all_masters = Masters.objects.all()
    return render(request, 'masters/masters_list.html', {'all_masters': all_masters})


def master_info(request, master_slug):
    master = get_object_or_404(Masters, slug=master_slug)
    return render(request, 'masters/master_info.html', {'master': master})
