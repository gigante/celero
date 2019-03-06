from django.contrib import admin
from django.contrib.auth import get_user_model
from .models.account import Account


User = get_user_model()


class MyAdminSite(admin.AdminSite):
    site_header = 'Celero'
    site_url = None
    index_title = 'Celero'


class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'full_name', 'last_login']
    ordering = ['username']

    def full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'

    full_name.short_description = 'nome'


class AccountModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'currency', 'flow']
    ordering = ['name', 'currency']


admin_site = MyAdminSite(name='myadmin')
admin_site.register(Account, AccountModelAdmin)
admin_site.register(User, UserModelAdmin)
