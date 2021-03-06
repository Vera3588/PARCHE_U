# Generated by Django 3.2.6 on 2022-03-18 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_gustos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estudiante',
            options={'verbose_name': 'estudiante', 'verbose_name_plural': 'estudiantes'},
        ),
        migrations.AlterModelOptions(
            name='gustos',
            options={'verbose_name': 'gusto', 'verbose_name_plural': 'gustos'},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'usuario', 'verbose_name_plural': 'usuarios'},
        ),
        migrations.AddField(
            model_name='usuario',
            name='foto_perfil',
            field=models.ImageField(null=True, upload_to='usuarios/images/foto_perfil/'),
        ),
    ]
