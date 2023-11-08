from django.contrib import admin
from .models import Services


class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Services, ServiceAdmin)
