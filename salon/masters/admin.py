from django.contrib import admin
from .models import Masters
from .models import Category


class MasterAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('first_name', 'second_name')}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category', )}


admin.site.register(Masters, MasterAdmin)
admin.site.register(Category, CategoryAdmin)
