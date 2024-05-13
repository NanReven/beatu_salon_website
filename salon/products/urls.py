from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_list, name='products_list'),
    path('<slug:product_slug>/', views.product_info, name='product_info'),
]
