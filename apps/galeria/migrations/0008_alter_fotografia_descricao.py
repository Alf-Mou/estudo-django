# Generated by Django 5.0.4 on 2024-07-29 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0007_alter_fotografia_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='descricao',
            field=models.CharField(max_length=150),
        ),
    ]