# Generated by Django 4.0.5 on 2022-06-28 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('imagem', models.ImageField(upload_to='images')),
                ('ano', models.CharField(max_length=10)),
                ('classificacao', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
                ('diretor', models.CharField(max_length=100)),
                ('sinopse', models.TextField()),
            ],
        ),
    ]
