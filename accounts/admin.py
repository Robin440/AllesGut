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



# admin.py

from django.contrib import admin
from django.contrib.sessions.models import Session
from accounts.models import User  # Import your custom user model
import pprint

class SessionAdmin(admin.ModelAdmin):
    list_display = ['session_key', 'user', 'session_data', 'expire_date']

    def session_data(self, obj):
        """Display session data in a readable format"""
        return pprint.pformat(obj.get_decoded(), indent=4)

    def user(self, obj):
        """Display the user associated with the session"""
        session_data = obj.get_decoded()
        user_id = session_data.get('_auth_user_id')
        if user_id:
            try:
                return User.objects.get(id=user_id)
            except User.DoesNotExist:
                return "User not found"
        return "Anonymous"

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(Session, SessionAdmin)




