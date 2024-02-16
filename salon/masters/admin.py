from django.contrib import admin
from .models import Masters
from .models import Categories


class MasterAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('first_name', 'second_name')}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ('first_name', )


admin.site.register(Masters, MasterAdmin)
admin.site.register(Categories, CategoryAdmin)
