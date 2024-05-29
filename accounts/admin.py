from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = (
        "email",
        "username",  
        "first_name",
        "last_name",
        "last_login",
        "date_joined",
        "is_active",
    )
    list_display_links = (
        "email",
        "username", 
        "first_name",
        "last_name",
    )
    readonly_fields = ("last_login", "date_joined")
    ordering = ("-date_joined",)

    filter_horizontal = ()
    list_filter = ("is_active", "is_staff", "is_superuser")
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}), 
        ('Personal info', {'fields': ('first_name', 'last_name', 'address', 'country')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )


# Register your CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
