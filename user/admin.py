
from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from .models import MyUser, UserProfile

        
class CustomUserAdmin(UserAdmin):
    model = MyUser
    list_display = [ 'username', 'phone', 'is_staff']
    list_display_links = ['username', 'phone']
    
    search_fields = ('username','phone',)
    readonly_fields=('date_joined', 'last_login')
     
    fieldsets = (
        (None, 
            {'fields': ('username', 'email', 'password', 'phone', 'national_id')}
        ),
        ('Permissions',
            {'fields': ('is_active', 'is_staff', 'groups')}
         ),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = ( (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'phone', 'national_id', 'is_staff')}
        ),
                     )
    
class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    readonly_fields=('user', 'birth_date', 'sex')


    
admin.site.register(MyUser, CustomUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
