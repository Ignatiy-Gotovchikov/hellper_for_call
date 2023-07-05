from django.contrib import admin
from django.contrib.admin import TabularInline

from breaks.models import organizations, replacements, groups, dicts, breaks

##############################
# INLINES
##############################
class ReplacementEmployeeInline(TabularInline):
    model = replacements.ReplacementEmployee
    fields = ('employee', 'status',)

@admin.register(organizations.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "director")


@admin.register(groups.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "manager", "min_active")
    search_fields = ('name',)


@admin.register(replacements.Replacement)
class ReplacementAdmin(admin.ModelAdmin):
    list_display = ("id", "group", "date", "break_start", "break_end", "break_max_duration")

    autocomplete_fields = ('group',)

    inlines = (ReplacementEmployeeInline,)


@admin.register(dicts.ReplacementStatus)
class ReplacementStatusAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "sort", "is_active", )\


@admin.register(dicts.BreakStatus)
class BreakStatusAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "sort", "is_active", )\


@admin.register(breaks.Break)
class BreakAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'replacement', 'break_start', 'break_end',
    )

