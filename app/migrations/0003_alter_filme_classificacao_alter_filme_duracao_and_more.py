# Generated by Django 4.0.5 on 2022-06-28 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_filme_duracao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='classificacao',
            field=models.CharField(max_length=100, verbose_name='classificação'),
        ),
        migrations.AlterField(
            model_name='filme',
            name='duracao',
            field=models.CharField(max_length=5, verbose_name='duração'),
        ),
        migrations.AlterField(
            model_name='filme',
            name='genero',
            field=models.CharField(max_length=100, verbose_name='gênero'),
        ),
        migrations.AlterField(
            model_name='filme',
            name='titulo',
            field=models.CharField(max_length=100, unique=True, verbose_name='título'),
        ),
    ]