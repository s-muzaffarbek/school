from django.contrib import admin
from .models import CustomUser, Subject, Test, StudentResult
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Role', {'fields': ('role',)}),
    )


admin.site.register(Subject)
admin.site.register(Test)
admin.site.register(StudentResult)
