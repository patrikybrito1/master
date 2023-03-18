# Generated by Django 4.1.7 on 2023-03-18 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0012_remove_livros_turma'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turma',
            name='color',
        ),
        migrations.AddField(
            model_name='livros',
            name='nome_turma',
            field=models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='turma',
            name='nome_turma',
            field=models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], max_length=50, null=True),
        ),
    ]
