from django.shortcuts import render
from website.forms import CadastroForm
from website.forms import AlagouForm
from website.models import *
# Create your views here.

def layout(request):
    return render(request, 'layout.html')

def home(request):
    return render(request, 'home.html')

def alagou(request):
    form = AlagouForm(request.POST or None)
    if form.is_valid():
        form.save()
        context = {
            'msg': "Alagamento cadastrado com sucesso"
        }
        return render(request, 'alagou.html', context)
    context = {
        'formulario':form
    }
    return render(request, 'alagou.html', context)

def cadastro(request):
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        form.save()
        context = {
            'msg': "Cadastro efetuado com sucesso"
        }
        return render(request, 'cadastro.html', context)
    context = {
        'formulario':form
    }
    return render(request, 'cadastro.html', context)