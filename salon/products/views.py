from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product, ProductCategory


def products_list(request):
    products = Product.objects.order_by('pk')
    categories = ProductCategory.objects.all()
    selected_category = request.GET.get('category')

    if selected_category is not None:
        if selected_category == '':
            products = Product.objects.all()
        else:
            selected_category = ProductCategory.objects.get(name=selected_category)
            products = products.filter(category=selected_category)

    paginator = Paginator(products, 9)  # Разбиваем на страницы, по 10 товаров на каждой
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'products/products_list.html', context)


def product_info(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'products/product_info.html', {'product': product})

