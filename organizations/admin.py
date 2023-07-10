from django.contrib import admin
from django.contrib.admin import TabularInline

from breaks.models.replacements import GroupInfo
from organizations.models import organizations, groups, dicts

##############################
# INLINES
##############################
class EmployeeInline(admin.TabularInline):
    model = organizations.Employee
    fields = ('user', 'position', 'date_joined',)


class MemberInline(admin.TabularInline):
    model = groups.Member
    fields = ('user', 'date_joined',)


class ProfileBreakInline(admin.StackedInline):
    model = GroupInfo
    fields = (
        'min_active',
        'break_start',
        'break_end',
        'break_max_duration',
    )


@admin.register(organizations.Organization)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director',)
    filter_vertical = ('employees',)

    inlines = (EmployeeInline,)


@admin.register(groups.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager', )
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    inlines = (
        ProfileBreakInline,
        MemberInline,
    )


@admin.register(dicts.Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "sort", "is_active", )




