from django.urls import path
from . import views

urlpatterns = [
    path('', views.services_list, name='services_list'),
    path('<slug:category_slug>/', views.category_info, name='category_info'),
    path('<slug:category_slug>/<slug:service_slug>/', views.service_info, name='service_info')
]
