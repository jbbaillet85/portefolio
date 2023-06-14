from django.contrib import admin
from apps.project.models import Project, Techno


# Register your models here.
class TechnoAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ["name"]


admin.site.register(Techno, TechnoAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "base_code", "slug")
    search_fields = ["name"]


admin.site.register(Project, ProjectAdmin)
