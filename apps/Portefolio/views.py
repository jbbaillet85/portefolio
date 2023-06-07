from models import Portefolio
from forms import PortefolioForm
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

class PortefolioCreateView(CreateView):
    model = Portefolio
    template_name = "Portefolio/create_Portefolio.html"
    form_class = PortefolioForm

class PortefolioUpdateView(UpdateView):
    model = Portefolio
    template_name = "Portefolio/update_Portefolio.html"
    form_class = PortefolioForm

class PortefolioDeleteView(DeleteView):
    model = Portefolio
    template_name = "Portefolio/delete_Portefolio.html"
    success_url = "/"  # Rediriger vers l'URL souhaitée après la suppression

class PortefolioDetailView(DetailView):
    model = Portefolio
    template_name = "Portefolio/detail_Portefolio.html"

class PortefolioListView(ListView):
    model = Portefolio
    template_name = "Portefolio/list_Portefolio.html"

