# Generated by Django 4.1.7 on 2023-03-29 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0024_remove_emprestimos_emprestimo_livros_emprestimo'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimos',
            name='emprestimos',
            field=models.BooleanField(default=False),
        ),
    ]
