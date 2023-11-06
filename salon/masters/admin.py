from django.contrib import admin
from .models import Masters
from .models import Speciality
from .models import MasterSpeciality

admin.site.register(Masters)
admin.site.register(Speciality)
admin.site.register(MasterSpeciality)
