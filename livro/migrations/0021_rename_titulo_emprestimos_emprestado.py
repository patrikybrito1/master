# Generated by Django 4.1.7 on 2023-03-25 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0020_alter_emprestimos_options_alter_livros_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emprestimos',
            old_name='titulo',
            new_name='emprestado',
        ),
    ]