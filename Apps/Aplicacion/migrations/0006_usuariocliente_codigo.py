# Generated by Django 4.1.1 on 2022-09-09 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0005_alter_carritocompra_idarticulo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariocliente',
            name='codigo',
            field=models.IntegerField(blank=True, null=True, verbose_name='codigo'),
        ),
    ]