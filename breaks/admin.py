from django.contrib import admin
from django.contrib.admin import TabularInline

from breaks.models import organizations, replacements
from breaks.models import groups

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
    list_display = ("id", "name", "manager", "min_active")\


@admin.register(replacements.Replacement)
class ReplacementAdmin(admin.ModelAdmin):
    list_display = ("id", "group", "date", "break_start", "break_end", "break_max_duration")

    inlines = (ReplacementEmployeeInline,)


@admin.register(replacements.ReplacementStatus)
class ReplacementStatusAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "sort", "is_active", )
