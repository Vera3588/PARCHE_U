# Generated by Django 3.2.6 on 2022-06-01 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0017_alter_publicaciones_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id_mensaje', models.IntegerField(primary_key=True, serialize=False)),
                ('mensaje', models.CharField(max_length=1000)),
                ('fecha_publicacion', models.CharField(max_length=10)),
                ('hora_publicacion', models.CharField(max_length=10)),
                ('usuario_envia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_enviador', to='usuarios.usuario')),
                ('usuario_recibe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_recibidor', to='usuarios.usuario')),
            ],
            options={
                'verbose_name': 'mensaje',
                'verbose_name_plural': 'mensajes',
            },
        ),
    ]
