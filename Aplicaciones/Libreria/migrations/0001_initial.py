# Generated by Django 4.2.2 on 2023-06-29 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=50)),
                ('precio', models.PositiveSmallIntegerField()),
                ('genero', models.CharField(max_length=50)),
            ],
        ),
    ]
