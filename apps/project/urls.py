from django.urls import path
from .views import (ProjectCreateView, ProjectUpdateView,
                    ProjectDeleteView, ProjectDetailView, ProjectListView)

app_name = 'apps.project'

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='project-create'),
    path('update/<int:pk>/', ProjectUpdateView.as_view(),
         name='project-update'),
    path('delete/<int:pk>/', ProjectDeleteView.as_view(),
         name='project-delete'),
    path('detail/<int:pk>/', ProjectDetailView.as_view(),
         name='project-detail'),
    path('list/', ProjectListView.as_view(), name='project-list'),
]
