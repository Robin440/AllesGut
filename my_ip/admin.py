from django.contrib import admin
from my_ip.models import MyIP
from member.models import Member

class MyIPAdmin(admin.ModelAdmin):
    # Display user details (email and first name) and other IP-related fields
    list_display = ('uuid', 'member_user_first_name', 'member_user_email', 'country_name', 'city', 'region')
    search_fields = ('uuid', 'member__user__first_name', 'member__user__email', 'country_name', 'city', 'region')  # Search via related fields
    list_filter = ('country_name', 'city', 'region')
    ordering = ('uuid',)
    readonly_fields = ['uuid']

    # Method to get the user's first name from the related Member model
    def member_user_first_name(self, obj):
        return obj.member.user.first_name
    member_user_first_name.admin_order_field = 'member__user__first_name'  # Enable sorting by first name
    member_user_first_name.short_description = 'User First Name'

    # Method to get the user's email from the related Member model
    def member_user_email(self, obj):
        return obj.member.user.email
    member_user_email.admin_order_field = 'member__user__email'  # Enable sorting by email
    member_user_email.short_description = 'User Email'

admin.site.register(MyIP, MyIPAdmin)
