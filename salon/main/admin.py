from django.contrib import admin
from .models import Users
from .models import Appointments

admin.site.register(Users)
admin.site.register(Appointments)
