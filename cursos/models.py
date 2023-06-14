from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Postagem(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    imagem = models.ImageField(null = True, blank = True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo