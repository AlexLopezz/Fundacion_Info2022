# Generated by Django 3.2 on 2022-08-29 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0003_evento_cantidad_dias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='cantidad_dias',
        ),
    ]
