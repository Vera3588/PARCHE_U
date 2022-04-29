# Generated by Django 4.0.2 on 2022-04-28 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_auto_20220427_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='amigos',
            field=models.ManyToManyField(blank=True, related_name='lista_amigos', to='usuarios.Usuario'),
        ),
        migrations.CreateModel(
            name='Solicitud_Amistad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario_envia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_envia', related_query_name='enviador', to='usuarios.usuario')),
                ('usuario_recibe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_recibe', related_query_name='recibidor', to='usuarios.usuario')),
            ],
        ),
    ]