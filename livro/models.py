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
   img = models.FileField(upload_to='capa_livro', null=True, blank=True)
   nome = models.CharField(max_length=80)
   autor = models.CharField(max_length=30)
   co_autor = models.CharField(max_length=30, blank=True, null=True)
   data_cadastro = models.DateField(default=date.today)

   def __str__(self) -> str:
       return self.nome
   class Meta:
       verbose_name = 'Livro'
   def get_queryset(self):
       txt_nome = self.request.GET.get('nome')
       livros = Livros.objects.filter(nome=txt_nome)
       return livros

class Emprestimos(models.Model):
    emprestado = models.ForeignKey(
       Livros, on_delete=models.DO_NOTHING, blank=True, null=True)
    nome_emprestado = models.CharField(blank=True, null=True, max_length=120)
    data_emprestimo = models.DateField(
       default=date.today, blank=True, null=True)
    data_devolucao = models.DateField(blank=True, null=True)
    tempo_duracao = models.DurationField(blank=True, null=True)
    usuario = models.ForeignKey(
       Usuario, on_delete=models.DO_NOTHING, blank=True, null=True)
    nome_turma = models.ForeignKey(
        Turma, on_delete=models.DO_NOTHING, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    def __str__(self) -> str:
       return self.usuario.nome
    class Meta:
       verbose_name = 'Emprestimo'
   
    def save(self, *args, **kwargs):
       if self.data_emprestimo and self.data_devolucao:
           self.tempo_duracao = self.data_devolucao - self.data_emprestimo
       else:
           self.tempo_duracao = None
       super(Emprestimos, self).save(*args, **kwargs)


    


  