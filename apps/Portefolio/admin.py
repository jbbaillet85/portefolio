from django.contrib import admin
from models import Portefolio

# Register your models here.
class PortefolioAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ["name"]


admin.site.register(Portefolio, PortefolioAdmin)