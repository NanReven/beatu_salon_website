from django.shortcuts import render


def services_list(request):
    return render(request, 'services/services_list.html')
