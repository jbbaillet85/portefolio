from django.urls import path, include
from apps.users.views import RegisterView

app_name = "apps.users"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path('register/', RegisterView.as_view(), name='register'),
]
