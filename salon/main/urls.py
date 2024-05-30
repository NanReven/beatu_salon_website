from django.urls import path
from django.views.generic import TemplateView

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
                  path('get_service_details/', views.get_service_details, name='get_service_details'),
                  path('account/<int:booking_id>/cancel_booking/', views.cancel_booking, name='cancel_booking'),
                  path('activate/<str:uidb64>/<str:token>/', views.activate_account, name='activate'),
                  path('account/', views.account, name='account'),
                  path('logout/', views.logoutUser, name='logout'),
                  path('account/schedule/', views.schedule, name='schedule'),
                  path('account/edit_profile/', views.edit_profile, name='edit_profile'),
                  path('account/change_password/', views.change_password, name='change_password'),
                  path('account/visits_history/', views.visits_history, name='visits_history'),
                  path('account/order_history/', views.order_history, name='order_history'),
                  path('account/booking/', views.booking, name='booking'),
                  path('account/booking/<int:booking_id>/accept/', views.accept_booking, name='accept_booking'),
                  path('account/booking/<int:booking_id>/decline/', views.decline_booking, name='decline_booking'),
                  path('cart/', views.cart, name='cart'),
                  path('reserve/', views.reserve, name='reserve'),
                  path('add_product/', views.add_product, name='add_product'),
                  path('get_cart_items/', views.get_cart_items, name='get_cart_items'),
                  path('remove_cart_item/', views.remove_cart_item, name='remove_cart_item'),
                  path('cancel_order/', views.cancel_order, name='cancel_order'),
                  path('password_reset/', views.password_reset_request, name='password_reset'),
                  path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
                  path('reset/done/', TemplateView.as_view(template_name='main/password_reset_complete.html'),
                       name='password_reset_complete'),
                  path('password_reset/done/',
                       TemplateView.as_view(template_name='main/password_reset_done.html'),
                       name='password_reset_done'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
