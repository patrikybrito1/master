from django.db import models
from datetime import date
from usuarios.models import Usuario, Turma
from django.db.models.signals import post_save
from django.dispatch import receiver

class Categoria(models.Model):
   nome = models.CharField(max_length=50)
   descricao = models.TextField()

   def __str__(self) -> str:
       return self.nome

class Livros(models.Model):
   
   img = models.FileField(upload_to='capa_livro', null=True, blank=True)
   nome = models.CharField(max_length=80, editable= True)
   autor = models.CharField(max_length=30)
   co_autor = models.CharField(max_length=30, blank=True, null=True)
   data_cadastro = models.DateField(default=date.today)
   categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
   esta_emprestado = models.BooleanField(editable=False, default=False)
   quantidade = models.PositiveIntegerField(default=1)  

   def __str__(self) -> str:
       return self.nome
   
   class Meta:
       verbose_name = 'Livro'

   def get_queryset(self):
       txt_nome = self.request.GET.get('nome')
       livros = Livros.objects.filter(nome=txt_nome)
       return livros

   
   def save(self, *args, **kwargs):
       if self.quantidade == 0:
           self.nome = f'{self.nome} (Indisponível)'
           self.editable = False
       else:
           self.editable = True
       super().save(*args, **kwargs)

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
    esta_emprestado = models.BooleanField(default=False)

    def hidden_livro(self):
        if self.emprestado.quantidade == 0:
            self.emprestado.nome = False
            self.save()

    def __str__(self) -> str:
       return self.emprestado.nome
    
    class Meta:
       verbose_name = 'Emprestimo'

    def delete(self, *args, **kwargs):
       self.esta_emprestado = False
       self.save()

    def save( self, *args, **kwargs):
       test = self.emprestado
       test.esta_emprestado = self.esta_emprestado
       test.save()
         
       if self.data_emprestimo and self.data_devolucao:
           self.tempo_duracao = self.data_devolucao - self.data_emprestimo
       else:
           self.tempo_duracao = None
       super(Emprestimos, self).save(*args, **kwargs)

@receiver(post_save, sender=Emprestimos)
def update_quantidade_livro(sender, instance, **kwargs):
        if instance.esta_emprestado:
        # Obtenha o objeto Livros correspondente ao empréstimo
            livro = instance.emprestado
        # Subtraia 1 da classe quantidade do objeto Livros
            livro.quantidade -= 1
        # Salve o objeto Livros atualizado
            livro.save()

@receiver(post_save, sender=Emprestimos)
def update_quantidade_livro(sender, instance, **kwargs):
    if not instance.esta_emprestado:
        # Obtenha o objeto Livros correspondente ao empréstimo
        livro = instance.emprestado
        # Adicione 1 à classe quantidade do objeto Livros
        livro.quantidade += 1
        # Salve o objeto Livros atualizado
        livro.save()
