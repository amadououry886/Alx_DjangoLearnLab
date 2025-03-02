from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """Customize the admin panel for CustomUser"""

    # Fields to be displayed in the admin panel
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

    # Fields to filter users in the admin panel
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    # Fields to search for users
    search_fields = ('username', 'email', 'first_name', 'last_name')

    # Define fieldsets (grouping fields when editing a user)
    fieldsets = (
        ('Personal Info', {'fields': ('username', 'email', 'first_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Fields shown when creating a user in the admin panel
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active'),
        }),
    )

    ordering = ('email',)  # Sort users by email in the admin panel

# Register the custom user model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)

