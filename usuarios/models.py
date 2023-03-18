from django.db import models

class Turma(models.Model):
  
    nome_turma = models.CharField(max_length=50,blank=True, null=True)
    
  
#    color = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')
    def __str__(self) -> str:
       return self.nome_turma
    
class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    senha = models.CharField(max_length=64)

    nome_turma = models.ForeignKey(
        Turma, on_delete=models.DO_NOTHING, blank=True, null=True)
    
    def __str__(self) -> str:
       return self.nome_turma


    def __str__(self) -> str:
        return self.nome



