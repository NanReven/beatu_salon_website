from django.urls import path
from . import views

urlpatterns = [
    path('', views.services_list, name='services_list'),
    path('<slug:category_slug>/', views.category_info, name='category_info'),
]
