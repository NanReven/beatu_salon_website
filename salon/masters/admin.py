from django.contrib import admin

from .forms import MasterForm
from .models import Masters
from .models import Users
from .models import Position
from .models import Weekday
from services.models import MasterCategory


class UserAdmin(admin.ModelAdmin):
    exclude = ('is_superuser', 'is_staff', 'groups', 'user_permissions')


admin.site.register(Position)
admin.site.register(Users, UserAdmin)
admin.site.register(MasterCategory)
admin.site.register(Weekday)


@admin.register(Masters)
class MasterAdmin(admin.ModelAdmin):
    form = MasterForm
