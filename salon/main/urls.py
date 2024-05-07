from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home_page'),
    path('registration/', views.registrate, name='registration'),
    path('login/', views.loginUser, name='login'),
    path('get_appointments/', views.get_appointments, name='get_appointments'),
    path('get_master_services/', views.get_master_services, name='get_master_services'),
    path('get_master_weekends/', views.get_master_weekends, name='get_master_weekends'),
    path('account/<int:booking_id>/cancel_booking/', views.cancel_booking, name='cancel_booking'),
    path('activate/<str:uidb64>/<str:token>/', views.activate_account, name='activate'),
    path('account/', views.account, name='account'),
    path('logout/', views.logoutUser, name='logout'),
    path('account/schedule/', views.schedule, name='schedule'),
    path('account/edit_profile/', views.edit_profile, name='edit_profile'),
    path('account/change_password/', views.change_password, name='change_password'),
    path('account/visits_history/', views.visits_history, name='visits_history'),
    path('account/booking/', views.booking, name='booking'),
    path('account/booking/<int:booking_id>/accept/', views.accept_booking, name='accept_booking'),
    path('account/booking/<int:booking_id>/decline/', views.decline_booking, name='decline_booking'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
