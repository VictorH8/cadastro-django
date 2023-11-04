from django.shortcuts import render
from .models import Usuario


# Create your views here.

def home(request):
    return render(request,'usuarios/home.html')

def listagem(request):
    new_user = Usuario()
    new_user.nome = request.POST.get('nome')
    new_user.idade = request.POST.get('idade')
    new_user.save()
    usuarios = {
        'usuarios': Usuario.objects.all()
    } 
    return render(request,'usuarios/listagem.html',usuarios)