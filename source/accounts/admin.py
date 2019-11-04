from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from accounts.models import Url


class UrlInline(admin.StackedInline):
    model = Url
    fields = ['description', 'avatar']


class ProfileAdmin(UserAdmin):
    inlines = [UrlInline]


admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)

