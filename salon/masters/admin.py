from django.contrib import admin
from .models import Masters
from .models import Speciality
from .models import MasterSpeciality


class MasterAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('first_name', 'second_name')}


admin.site.register(Masters, MasterAdmin)
admin.site.register(Speciality)
admin.site.register(MasterSpeciality)
