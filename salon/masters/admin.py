from django.contrib import admin
from .models import Masters
from .models import Users
from .models import Position


class UserAdmin(admin.ModelAdmin):
    exclude = ('is_superuser', 'is_staff', 'groups', 'user_permissions')


admin.site.register(Masters)
admin.site.register(Position)
admin.site.register(Users, UserAdmin)
