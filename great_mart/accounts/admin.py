from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# Register your models here.
class AdminUser(UserAdmin):
    list_display = [
        'username',
        'email',
        'is_staff',
        'is_active',
        'is_superadmin',
        'is_admin'
    ]
    filter_horizontal = ()
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = [
        (
            None,
            {
                'fields': ['email', ('first_name', 'last_name')],
            },
        ),
        (
            'Advanced options',
            {
                'classes': ['collapse'],
                'fields': ['password', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'],
            },
        ),
    ]



admin.site.register(models.CustomUserModel, AdminUser)
