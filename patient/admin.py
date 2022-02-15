from django.contrib import admin
from .models import UserVital, Appointments




class UserVitalAdmin(admin.ModelAdmin):
    model = UserVital
    readonly_fields=('user',)


admin.site.register(UserVital, UserVitalAdmin)
admin.site.register(Appointments)