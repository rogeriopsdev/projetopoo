from restauranteapp.models import Mesa
from django import forms


# cria formulário

class MesaForms(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = "__all__"
