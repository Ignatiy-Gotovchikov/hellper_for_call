from django.contrib import admin

from breaks.models import organizations


@admin.register(organizations.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "director")


@admin.register(organizations.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "manager", "min_active")
