# Generated by Django 3.2 on 2022-08-17 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0003_alter_noticia_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='descripciones',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
