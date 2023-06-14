from django.contrib import admin
from apps.portefolio.models import Portefolio


# Register your models here.
class PortefolioAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ["name"]


admin.site.register(Portefolio, PortefolioAdmin)
