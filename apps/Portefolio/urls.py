from django.urls import path
from .views import (
    PortefolioCreateView,
    PortefolioUpdateView,
    PortefolioDeleteView,
    PortefolioDetailView,
    PortefolioListView,
)

app_name = "apps.portefolio"

urlpatterns = [
    path("", PortefolioListView.as_view(), name="Portefolio_list"),
    path("create/", PortefolioCreateView.as_view(), name="Portefolio_create"),
    path("<slug:slug>/", PortefolioDetailView.as_view(),
         name="Portefolio_detail"),
    path("<slug:slug>/update/", PortefolioUpdateView.as_view(),
         name="Portefolio_update"),
    path("<slug:slug>/delete/", PortefolioDeleteView.as_view(),
         name="Portefolio_delete"),
]
