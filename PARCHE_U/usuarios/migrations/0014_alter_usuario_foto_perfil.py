# Generated by Django 3.2.6 on 2022-05-24 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0013_auto_20220524_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto_perfil',
            field=models.ImageField(default='foto_perfil/nullprofile.jpg', upload_to='foto_perfil'),
        ),
    ]