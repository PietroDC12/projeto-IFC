# Generated by Django 3.1.3 on 2020-11-16 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TbCampanha',
            fields=[
                ('campanha_id', models.AutoField(primary_key=True, serialize=False)),
                ('ativo', models.BooleanField(default=False)),
                ('titulo_campanha', models.CharField(max_length=100)),
                ('desc_campanha', models.TextField(max_length=1400)),
                ('dt_inicio_campanha', models.DateField()),
                ('dt_fim_campanha', models.DateField()),
                ('rua_campanha', models.CharField(max_length=100)),
                ('numero_endereco_campanha', models.CharField(max_length=10)),
                ('bairro_campanha', models.CharField(max_length=100)),
                ('cidade_campanha', models.CharField(max_length=100)),
                ('link_campanha', models.URLField()),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='campanhas', to='pessoas.tbpessoa')),
            ],
            options={
                'verbose_name': 'Campanha',
                'verbose_name_plural': 'Campanhas',
            },
        ),
    ]
