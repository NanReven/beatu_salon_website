from django.contrib import admin
from .models import Masters
from .models import Users
from .models import Position


'''class MasterAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('first_name', 'second_name')}
'''


#admin.site.register(Masters, MasterAdmin)
admin.site.register(Masters)
admin.site.register(Position)
admin.site.register(Users)
