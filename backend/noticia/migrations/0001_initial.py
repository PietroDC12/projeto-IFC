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
            name='TbNoticia',
            fields=[
                ('noticia_id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo_noticia', models.CharField(max_length=300)),
                ('subtitulo_noticia', models.CharField(max_length=300)),
                ('desc_noticia', models.TextField(max_length=10000)),
                ('pessoas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='noticia', to='pessoas.tbpessoa')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
            },
        ),
    ]