from django.contrib import admin
from .models import Appointments, AppointmentService


class AppointmentServiceInline(admin.TabularInline):
    model = AppointmentService
    extra = 1


class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'master', 'start_datetime', 'end_datetime', 'status', 'total_sum')
    list_filter = ('status', 'master', 'start_datetime', 'end_datetime')
    search_fields = ('user__username', 'master__user__username', 'comment')
    date_hierarchy = 'start_datetime'
    inlines = [AppointmentServiceInline]
    fieldsets = (
        (None, {
            'fields': ('user', 'master', 'status')
        }),
        ('Дата и время', {
            'fields': ('start_datetime', 'end_datetime')
        }),
        ('Детали', {
            'fields': ('comment', 'total_sum')
        }),
    )
    readonly_fields = ('total_sum',)


admin.site.register(Appointments, AppointmentsAdmin)


class AppointmentServiceAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'service', 'get_master', 'get_user', 'get_start_datetime')
    list_filter = ('service', 'appointment__master', 'appointment__start_datetime')
    search_fields = ('service__title', 'appointment__user__username', 'appointment__master__user__username')

    def get_master(self, obj):
        return obj.appointment.master.user.last_name + ' ' + obj.appointment.master.user.last_name

    get_master.short_description = 'Мастер'

    def get_user(self, obj):
        return obj.appointment.user.first_name + ' ' + obj.appointment.user.last_name

    get_user.short_description = 'Посетитель'

    def get_start_datetime(self, obj):
        return obj.appointment.start_datetime

    get_start_datetime.short_description = 'Дата и время начала'


admin.site.register(AppointmentService, AppointmentServiceAdmin)
