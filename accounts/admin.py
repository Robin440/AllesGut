from django.contrib import admin
from accounts.models import User,VerificationToken

# Register your models here.

# Registering user model for admin.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(User,UserAdmin)


class VerificationTokenAdmin(admin.ModelAdmin):
    list_display = ('uuid','name', 'token', 'otp')
    list_filter = ('name', 'token')
    search_fields = ('uuid', 'name', 'token','otp')
    ordering = ('uuid',)
    readonly_fields=['uuid']

admin.site.register(VerificationToken,VerificationTokenAdmin)



