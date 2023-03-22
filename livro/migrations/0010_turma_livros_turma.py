# Generated by Django 4.1.7 on 2023-03-17 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0009_alter_livros_data_emprestimo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_turma', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='livros',
            name='turma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='livro.turma'),
        ),
    ]