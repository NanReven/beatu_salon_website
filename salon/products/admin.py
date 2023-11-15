from django.contrib import admin
from .models import Products


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Products, ProductAdmin)
