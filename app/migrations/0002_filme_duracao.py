# Generated by Django 4.0.5 on 2022-06-28 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='duracao',
            field=models.CharField(default='', max_length=5),
            preserve_default=False,
        ),
    ]
