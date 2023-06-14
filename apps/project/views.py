from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, UpdateView,
                                  DeleteView, DetailView, ListView)
from django.urls import reverse_lazy
from .models import Project


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "project/create_project.html"
    fields = ['name', 'description', 'techno', 'base_code']
    success_url = reverse_lazy('project-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = "project/update_project.html"
    fields = ['name', 'description', 'techno', 'base_code']

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = "project/delete_project.html"
    success_url = reverse_lazy('project-list')

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ProjectDetailView(DetailView):
    model = Project
    template_name = "project/detail_project.html"


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "project/list_project.html"
    context_object_name = 'projects'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
