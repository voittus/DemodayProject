from django import forms
from website.models import Cadastro
from website.models import Alagou
from django.contrib.auth.models import User



class CadastroForm(forms.ModelForm):
    User._meta.get_field('email').blank = False
    User._meta.get_field('password').blank = False
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]
        widgets = {
            'username':forms.TextInput(attrs={'class': 'form-control', 'maxlength':140 }),
            'password':forms.PasswordInput(attrs={'class': 'form-control', 'maxlength':255 })
        }
    def save(self, commit=True):
        user = super(CadastroForm, self).save(commit = False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class AlagouForm(forms.ModelForm):
    class Meta:
        model = Alagou
        fields = [
            'rua',
            'bairro',
            'trafego',
        ]

