from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from .forms import MasterForm
from .models import Masters
from .models import Users
from .models import Position
from .models import Weekday
from services.models import MasterCategory


class CustomUserAdmin(UserAdmin):
    model = Users
    exclude = ('is_superuser', 'is_staff', 'groups', 'user_permissions')
    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'is_customer', 'is_active')
    list_filter = ('is_customer', 'is_active')
    search_fields = ('email', 'first_name', 'last_name', 'phone_number')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Личные данные', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Информация об аккаунте', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone_number', 'password1', 'password2', 'is_customer', 'is_staff', 'is_active')}
        ),
    )


admin.site.register(Users, CustomUserAdmin)


@admin.register(Masters)
class MasterAdmin(admin.ModelAdmin):
    form = MasterForm

admin.site.register(Position)
admin.site.register(MasterCategory)
admin.site.register(Weekday)
