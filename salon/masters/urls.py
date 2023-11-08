from django.urls import path
from . import views

urlpatterns = [
    path('', views.masters_list, name='masters_list'),
    path('masters/<slug:master_slug>/', views.master_info, name='master_info')
]
