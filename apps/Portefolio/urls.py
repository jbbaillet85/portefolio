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
    path("<int:pk>/", PortefolioDetailView.as_view(),
         name="Portefolio_detail"),
    path("<int:pk>/update/", PortefolioUpdateView.as_view(),
         name="Portefolio_update"),
    path("<int:pk>/delete/", PortefolioDeleteView.as_view(),
         name="Portefolio_delete"),
]
