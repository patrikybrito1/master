# Generated by Django 4.1.7 on 2023-03-29 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0027_alter_emprestimos_emprestimo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimos',
            name='emprestimo',
        ),
    ]
