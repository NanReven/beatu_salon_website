from django.urls import path
from . import views

urlpatterns = [
    path('', views.masters_list, name='masters_list')
]
