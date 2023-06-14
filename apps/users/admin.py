from django.contrib import admin
from django.contrib.auth import get_user_model
from apps.users.models import Skill

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email")


admin.site.register(User, UserAdmin)


class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ["name"]


admin.site.register(Skill, SkillAdmin)
