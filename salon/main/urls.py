from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home_page'),
    path('registration/', views.registrate, name='registration'),
    path('authorization/', views.auth, name='auth')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)