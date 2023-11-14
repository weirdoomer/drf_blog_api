from django.contrib import admin

from users.models import User, Profile


class ProfileInline(admin.TabularInline):
    model = Profile
    fields = ['user', 'bio', 'avatar', 'is_author']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    inlines = [ProfileInline]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'avatar', 'is_author']
