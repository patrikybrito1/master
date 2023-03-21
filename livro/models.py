from django.db import models
from datetime import date, timedelta
from usuarios.models import Usuario, Turma
from django.contrib import admin



class Categoria(models.Model):
   nome = models.CharField(max_length=50)
   descricao = models.TextField()


   def __str__(self) -> str:
       return self.nome


class Livros(models.Model):
   nome = models.CharField(max_length=80)
   autor = models.CharField(max_length=30)
   co_autor = models.CharField(max_length=30, blank=True, null=True)
   data_cadastro = models.DateField(default=date.today)
   emprestado = models.BooleanField(default=False)
   nome_emprestado = models.CharField(blank=True, null=True, max_length=120)
   data_emprestimo = models.DateField(
       default=date.today, blank=True, null=True)
   data_devolucao = models.DateField(blank=True, null=True)
   tempo_duracao = models.DurationField(blank=True, null=True)
   categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
   usuario = models.ForeignKey(
       Usuario, on_delete=models.DO_NOTHING, blank=True, null=True)
   nome_turma = models.ForeignKey(
        Turma, on_delete=models.DO_NOTHING, blank=True, null=True)
#    nome_turma = models.CharField(max_length=20, choices=Turma.lista_turma, null=True)
   



   def save(self, *args, **kwargs):
       if self.data_emprestimo and self.data_devolucao:
           self.tempo_duracao = self.data_devolucao - self.data_emprestimo
       else:
           self.tempo_duracao = None
       super(Livros, self).save(*args, **kwargs)


   def get_queryset(self):
       txt_nome = self.request.GET.get('nome')
       livros = Livros.objects.filter(nome=txt_nome)
       return livros


   class Meta:
       verbose_name = 'Livro'


   def __str__(self) -> str:
       return self.nome