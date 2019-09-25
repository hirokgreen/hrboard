from django.contrib import admin

from .models import Project, Works

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Project, ProjectAdmin)


class WorksAdmin(admin.ModelAdmin):
    list_display = (
        'employee', 'project', 'date', 'location',
        'working_hour', 'is_cod',
    )

    list_filter = ('employee', 'project', 'working_hour', 'location')
    search_fields = ('project__name', 'employee__username')
    date_hierarchy = 'date'

admin.site.register(Works, WorksAdmin)
