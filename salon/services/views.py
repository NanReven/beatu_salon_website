from django.shortcuts import render
from .models import Services


def services_list(request):
    all_services = Services.objects.all()
    return render(request, 'services/services_list.html', {'all_services': all_services})
