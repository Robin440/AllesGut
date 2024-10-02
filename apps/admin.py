from django.contrib import admin

# Register your models here.

from apps.models import App,Services


class  AppAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'name', 'is_active')
    list_filter = ('name','is_active')
    search_fields = ['name']
    list_per_page = 10
    readonly_fields=['uuid']


admin.site.register(App,AppAdmin)



class  ServiceAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'name', 'is_active')
    list_filter = ('name','is_active')
    search_fields = ['name']
    list_per_page = 10
    readonly_fields=['uuid']


admin.site.register(Services,ServiceAdmin)  # Register your models here.  # Register your