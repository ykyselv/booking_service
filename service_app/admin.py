from django.contrib import admin
from .models import Specialist, Client, Schedule, Appointment, Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['address']


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['start_appointment', 'end_appointment']
    list_per_page = 10


class SpecialistAdmin(admin.ModelAdmin):
    list_display = ['specialization', 'name']
    list_per_page = 10


class ClientAdmin(admin.ModelAdmin):
    list_display = ['gender', 'name']
    list_per_page = 10


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['start_appointment', 'end_appointment']
    list_per_page = 10


admin.site.register(Specialist, SpecialistAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Schedule, ScheduleAdmin)
