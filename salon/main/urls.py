from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home_page'),
    path('registration/', views.registrate, name='registration'),
    path('login/', views.loginUser, name='login'),
    path('activate/<str:uidb64>/<str:token>/', views.activate_account, name='activate'),
    path('account/', views.account, name='account'),
    path('logout/', views.logoutUser, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
