# Generated by Django 3.2 on 2022-08-29 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0010_auto_20220827_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='fechaCreacion',
            field=models.DateField(),
        ),
    ]
