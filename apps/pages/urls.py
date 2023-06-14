from django.urls import path
from .views import home_view, ProfilePageView

app_name = "pages"

urlpatterns = [
    path("", home_view, name="home"),
    path("profile/", ProfilePageView.as_view(), name="profile"),
]
