# Generated by Django 3.2.6 on 2022-06-01 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0016_alter_publicaciones_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicaciones',
            name='imagen',
            field=models.FileField(null=True, upload_to='publicaciones/'),
        ),
    ]