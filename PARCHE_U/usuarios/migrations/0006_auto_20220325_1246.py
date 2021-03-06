# Generated by Django 3.2.6 on 2022-03-25 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_remove_usuario_foto_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gustos',
            name='deportes',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='gustos',
            name='literatura',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='gustos',
            name='musica',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='gustos',
            name='series',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='gustos',
            name='videojuegos',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.CreateModel(
            name='Publicaciones',
            fields=[
                ('id_publicacion', models.IntegerField(primary_key=True, serialize=False)),
                ('mensaje', models.CharField(max_length=1000)),
                ('imagen', models.ImageField(null=True, upload_to='usuarios/images/publicaciones/')),
                ('fecha_publicacion', models.DateField()),
                ('hora_publicacion', models.TimeField()),
                ('codigo_estudiante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
            options={
                'verbose_name': 'publicacion',
                'verbose_name_plural': 'publicaciones',
            },
        ),
    ]
