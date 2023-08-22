# Generated by Django 4.2.4 on 2023-08-22 01:54

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField(max_length=1000)),
                ('foto', stdimage.models.StdImageField(force_min_size=False, upload_to='servicos', variations={'thumb': {'crop': True, 'height': 600, 'width': 600}})),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
                'ordering': ('nome',),
            },
        ),
    ]