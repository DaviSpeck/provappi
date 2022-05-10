from django.db import models

class Tipo(models.Model):

    id_tipo = models.IntegerField(primary_key=True, blank=False)
    nome = models.CharField(max_length=45, null=False, blank=False)

class StatusSenha(models.Model):

    id_status_senha = models.IntegerField(primary_key=True, blank=False)
    nome = models.CharField(max_length=45, null=False, blank=False)

class Categoria(models.Model):

    id_categoria = models.IntegerField(primary_key=True, blank=False)
    nome = models.CharField(max_length=45, null=False, blank=False)

class Senha(models.Model):

    id_senha = models.IntegerField(primary_key=True, blank=False)
    senha = models.IntegerField(null=False, blank=False)
    hora_data = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    id_status_senha = models.ForeignKey(StatusSenha, on_delete=models.CASCADE)
