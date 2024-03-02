from django.contrib import admin
from .models import Services
from .models import Categories


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ('title', )


class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Services, ServiceAdmin)
admin.site.register(Categories, CategoryAdmin)
