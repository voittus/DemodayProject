from django.shortcuts import render, get_object_or_404, redirect
from website.forms import CadastroForm
from website.forms import AlagouForm
from website.models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def layout(request):
    return render(request, 'layout.html')

def home(request):
    return render(request, 'home.html')

@login_required
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
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # context = {
            #     'msg': "Cadastro efetuado com sucesso"
            # }
        return render(request, 'cadastro.html')
    context = {
        'formulario':form
    }
    return render(request, 'cadastro.html', context)

def local(request):
    locals = Alagou.objects.all().order_by('bairro')
    return render(request, 'locaisalagados.html', {'locals': locals})

def login_user(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('')
    return render(request, 'login.html')