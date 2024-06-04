from django.contrib import admin
from .models import Services
from .models import Categories


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ('title', )


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'duration', 'cost',)
    list_filter = ('category',)
    search_fields = ('title', )
    list_editable = ('cost', 'duration', )
    fields = ('title', 'category', 'duration', 'cost',)


admin.site.register(Services, ServicesAdmin)
admin.site.register(Categories, CategoryAdmin)
