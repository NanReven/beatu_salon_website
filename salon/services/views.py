from django.shortcuts import render, get_object_or_404
from .models import Category, Services


def services_list(request):
    all_categories = Category.objects.all()
    return render(request, 'services/categories_list.html', {'all_categories': all_categories})


def category_info(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    all_services = Services.objects.all().filter(category_id=category.category_id)
    context = {
        'all_services': all_services,
        'category': category
    }
    return render(request, 'services/category_info.html', context)
