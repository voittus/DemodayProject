from django import forms
from website.models import Cadastro
from website.models import Alagou
class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = [
            
            'nome',
            'email',
            'senha',
        ]

class AlagouForm(forms.ModelForm):
    class Meta:
        model = Alagou
        fields = [
            'bairro',
            'situacao',
            'trafego',
        ]