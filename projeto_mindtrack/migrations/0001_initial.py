# Generated by Django 5.1.7 on 2025-04-05 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('usuarioID', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('senha', models.CharField(max_length=255)),
                ('idade', models.IntegerField()),
                ('sexo', models.CharField(max_length=20)),
            ],
        ),
    ]
