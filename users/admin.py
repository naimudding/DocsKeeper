from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin

from users.models import member

class AcountAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_admin', "is_staff")
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(member, AcountAdmin)