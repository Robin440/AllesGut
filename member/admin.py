from django.contrib import admin
from member.models import Member,MemberImage,Role
# Register your models here.

class RoleAdmin(admin.ModelAdmin):
    list_display = ('uuid','name','description')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields=['uuid']

admin.site.register(Role,RoleAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'user_first_name', 'user_email', 'created_at']  # Replace 'id' with 'uuid'
    list_filter = ('created_at',)
    search_fields = ('user__first_name', 'user__email')
    readonly_fields = ('uuid', 'created_at')

    # Method to get the user's first name
    def user_first_name(self, obj):
        return obj.user.first_name  # Assuming user is a ForeignKey
    user_first_name.admin_order_field = 'user__first_name'
    user_first_name.short_description = 'User First Name'

    # Method to get the user's email
    def user_email(self, obj):
        return obj.user.email
    user_email.admin_order_field = 'user__email'
    user_email.short_description = 'User Email'

admin.site.register(Member, MemberAdmin)




class MemberImageAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'member_user_first_name', 'member_user_email', 'created_at']
    list_filter = ('created_at',)
    search_fields = ('member__user__first_name', 'member__user__email')  # Search via related fields
    readonly_fields = ('uuid', 'created_at')

    # Method to get the member's user's first name
    def member_user_first_name(self, obj):
        return obj.member.user.first_name
    member_user_first_name.admin_order_field = 'member__user__first_name'
    member_user_first_name.short_description = 'User First Name'

    # Method to get the member's user's email
    def member_user_email(self, obj):
        return obj.member.user.email
    member_user_email.admin_order_field = 'member__user__email'
    member_user_email.short_description = 'User Email'

admin.site.register(MemberImage, MemberImageAdmin)
