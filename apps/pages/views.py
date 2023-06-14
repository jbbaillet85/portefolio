from django.views.generic import TemplateView
from apps.portefolio.models import Portefolio
from apps.project.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        portefolios = Portefolio.objects.all()
        context['portefolios'] = portefolios
        return context


home_view = HomeView.as_view()


class ProfilePageView(LoginRequiredMixin, TemplateView):
    template_name = "pages/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        projects = user.projects.all()
        context['user'] = user
        context['projects'] = projects
        return context
