# Generated by Django 5.0.6 on 2024-11-15 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.CharField(default='', max_length=100, primary_key=True, serialize=False)),
                ('nome', models.CharField(default='', max_length=150)),
                ('cpf', models.CharField(default='', max_length=14)),
                ('telefone', models.CharField(default='', max_length=15)),
                ('email', models.EmailField(default='', max_length=254)),
                ('cep', models.CharField(default='', max_length=9)),
                ('logradouro', models.CharField(default='', max_length=150)),
                ('numero', models.CharField(default='', max_length=10)),
                ('complemento', models.CharField(default='', max_length=150)),
                ('bairro', models.CharField(default='', max_length=100)),
                ('cidade', models.CharField(default='', max_length=100)),
                ('uf', models.CharField(default='', max_length=2)),
            ],
        ),
    ]
