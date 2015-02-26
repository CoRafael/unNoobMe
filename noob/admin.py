from django.contrib import admin

from noob.models import UserProfile


class UserProfilePageAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'firstname', 'last_name', 'email', 'city', 'points', 'last_login', 'date_joined', 'avatar',)


admin.site.register(UserProfile, UserProfilePageAdmin)


# Register your models here.
