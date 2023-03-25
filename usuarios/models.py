from django.db import models

class Turma(models.Model):
  
    nome = models.CharField(max_length=50,blank=True, null=True)

    def __str__(self) -> str:
        return self.nome

    

class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    senha = models.CharField(max_length=64)
    telefone = models.CharField(max_length=11)
    turma = models.ForeignKey(
        Turma, on_delete=models.DO_NOTHING,blank=True, null=True)
    
    def __str__(self) -> str:
       return self.turma


    def __str__(self) -> str:
        return self.nome



