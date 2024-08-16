from django import froms
from .models import personas

class personaForm(forms.ModelForm):
    class meta:
        model = persona
        fields = '__all__'