from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, forgotPassword

class AccountAdmin(UserAdmin):
    list_display = ('name', 'phone_number', 'last_login', 'date_joined')
    list_display_links = ('name', 'phone_number')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
admin.site.register(forgotPassword)