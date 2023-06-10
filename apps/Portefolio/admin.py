from django.contrib import admin
from apps.portefolio.models import Portefolio, Skill, Techno, Project, Developer


# Register your models here.
class PortefolioAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ["name"]


admin.site.register(Portefolio, PortefolioAdmin)


class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ["name"]


admin.site.register(Skill, SkillAdmin)


class TechnoAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ["name"]


admin.site.register(Techno, TechnoAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ["name"]


admin.site.register(Project, ProjectAdmin)


class DeveloperAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ["name"]


admin.site.register(Developer, DeveloperAdmin)
