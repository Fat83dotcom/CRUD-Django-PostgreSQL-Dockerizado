from django import forms
from Core.models import CadastroCliente


class CadastroForm(forms.ModelForm):
    class Meta:
        model = CadastroCliente
        fields = ('nome', 'nasc', 'email', 'cidade')
