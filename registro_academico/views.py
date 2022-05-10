from django.shortcuts import render
from registro_academico.models import Senha, Categoria, StatusSenha, Tipo

def index(request):

	return render(request, 'index.html', {'senhas': Senha.objects.all()})

