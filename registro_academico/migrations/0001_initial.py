# Generated by Django 2.2 on 2022-05-10 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='StatusSenha',
            fields=[
                ('id_status_senha', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id_tipo', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Senha',
            fields=[
                ('id_senha', models.IntegerField(primary_key=True, serialize=False)),
                ('senha', models.IntegerField()),
                ('hora_data', models.DateTimeField(auto_now_add=True)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro_academico.Categoria')),
                ('id_status_senha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro_academico.StatusSenha')),
                ('id_tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro_academico.Tipo')),
            ],
        ),
    ]
