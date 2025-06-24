from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Estudiante, Profesor, Curso, Entregable
# Register your models here.

admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Entregable)

class UserAdmin(BaseUserAdmin):

    list_display = ("username", "email", "first_name", "last_name")
    search_fields = ("username", "first_name", "last_name", "email")
    readonly_fields = ("date_joined", "last_login")

    fieldsets = (
        ("Admin", {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
