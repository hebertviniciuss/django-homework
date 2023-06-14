from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import Curso, Postagem
# Create your views here.
def index(request: HttpRequest):
    cursos = Curso.objects.all()
    context = {"cursos" : cursos}
    return render(request, "index.html", context)

def postagens(request: HttpRequest, curso_id: int):
    postagens = Postagem.objects.filter(curso=curso_id)
    context = {"postagens": postagens}
    return render(request,"postagens.html", context)

def postagem(request: HttpRequest, postagem_id: int):
    postagem = Postagem.objects.get(id=postagem_id)
    context = {"postagem": postagem}
    return render(request, "postagem.html", context)