# Generated by Django 4.1 on 2022-09-08 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0004_rename_invetario_inventario_alter_inventario_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carritocompra',
            name='idArticulo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Aplicacion.articulo'),
        ),
        migrations.AlterField(
            model_name='carritocompra',
            name='idUsuarioCliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Aplicacion.usuariocliente'),
        ),
        migrations.AlterField(
            model_name='facturacion',
            name='idCarritoCompra',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Aplicacion.carritocompra'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='idArticulo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Aplicacion.articulo'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='idUsuarioAdmin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Aplicacion.usuarioadmin'),
        ),
    ]