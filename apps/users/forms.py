from apps.users.models import Skill
from django import forms


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']
