from django.db import models
from django.utils.timezone import now

# Create your models here.
class Grupo(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    status = models.CharField(max_length=15, default="Ativo")
    data_criacao = models.DateTimeField(default=now)

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nome_completo = models.CharField(max_length=100)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=15)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    pais = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    logradouro = models.CharField(max_length=100)
    status = models.CharField(max_length=15, default="Ativo")

    grupo = models.ForeignKey(Grupo, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nome_completo