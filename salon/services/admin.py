from django.contrib import admin
from .models import Services
from .models import ServiceSpeciality
from .models import Category
from .models import CategoryService


class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Services, ServiceAdmin)
admin.site.register(ServiceSpeciality)
admin.site.register(Category)
admin.site.register(CategoryService)
