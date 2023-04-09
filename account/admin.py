from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AppUser
# Register your models here.


@admin.register(AppUser)
class AppUserAdmin(UserAdmin):

    list_display = ('username', 'email', 'role', 'is_dentist')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('color',)}),
        ("Role", {'fields': ('role',)})
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'classes': ('wide',), "fields": ("role",)}),
    )

