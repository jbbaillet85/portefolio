from apps.portefolio.models import Portefolio
from django import forms


class PortefolioForm(forms.ModelForm):

    class Meta:
        model = Portefolio
        fields = [
            'name',
        ]
        help_texts = {
            'name': 'Le nom de Portefolio',
        }
