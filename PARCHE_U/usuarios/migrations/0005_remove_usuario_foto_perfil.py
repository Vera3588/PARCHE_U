# Generated by Django 3.2.6 on 2022-03-19 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20220318_1854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='foto_perfil',
        ),
    ]