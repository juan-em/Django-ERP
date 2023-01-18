# Generated by Django 3.2 on 2023-01-18 18:17

import app.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=500)),
                ('descripcion_corta', models.CharField(max_length=100)),
                ('stock', models.PositiveIntegerField()),
                ('stock_minimo', models.PositiveIntegerField()),
                ('aviso_minimo', models.CharField(choices=[('Sí', 'Sí'), ('No', 'No')], max_length=3)),
                ('datos_producto', models.CharField(max_length=500)),
                ('fecha_alta', models.DateTimeField()),
                ('unidades_por_caja', models.PositiveIntegerField()),
                ('observaciones', models.CharField(max_length=500)),
                ('precio_compra', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('precio_tienda', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('imagen', models.ImageField(null=True, upload_to=app.models.upload_path)),
            ],
        ),
        migrations.CreateModel(
            name='Caja_diaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(null=True)),
                ('monto_total_inicial', models.FloatField(null=True)),
                ('monto_total_final', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Compra_linea_prov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio', models.FloatField()),
                ('importe', models.FloatField(null=True)),
                ('dsctoproducto', models.FloatField(blank=True, default=0, null=True)),
                ('codproducto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.articulos')),
            ],
        ),
        migrations.CreateModel(
            name='Embalajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('estructurajuridica', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('localidad', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=500)),
                ('codpostal', models.CharField(max_length=100)),
                ('cuentabancaria', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('movil', models.CharField(max_length=100)),
                ('web', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Entidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreentidad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(null=True)),
                ('iva', models.IntegerField()),
                ('totalfactura', models.FloatField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Factura_linea_clie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio', models.FloatField()),
                ('importe', models.FloatField(null=True)),
                ('dsctoproducto', models.FloatField()),
                ('codproducto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.articulos')),
            ],
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Formapago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrefp', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Impuestos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('valor', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=100)),
                ('localidad', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=500)),
                ('codpostal', models.CharField(max_length=100)),
                ('cuentabancaria', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('movil', models.CharField(max_length=100)),
                ('web', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField(default=0)),
                ('descripcion_producto', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Provincias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreprovincia', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Remision_clie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Remision_prov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Ubicaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.persona')),
                ('borrado', models.CharField(default=0, max_length=1)),
                ('codformapago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.formapago')),
            ],
        ),
        migrations.CreateModel(
            name='Compra_prov',
            fields=[
                ('compra', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.factura')),
                ('imagen_factura_compra', models.ImageField(blank=True, null=True, upload_to=app.models.upload_path2)),
                ('estado', models.BooleanField(blank=True, default=False, null=True)),
                ('detaller_entrega', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Factura_clie',
            fields=[
                ('factura', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.factura')),
                ('codcliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.clientes')),
            ],
        ),
        migrations.CreateModel(
            name='Remision_linea_prov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codproducto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.compra_linea_prov')),
                ('codremision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.remision_prov')),
            ],
        ),
        migrations.CreateModel(
            name='Remision_linea_clie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codproducto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.factura_linea_clie')),
                ('codremision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.remision_clie')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruc', models.CharField(max_length=100)),
                ('borrado', models.CharField(default=0, max_length=1)),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.empresa')),
                ('persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Producto_detalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.articulos')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='codprovincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.provincias'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='codprovincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.provincias'),
        ),
        migrations.AddField(
            model_name='articulos',
            name='embalaje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.embalajes'),
        ),
        migrations.AddField(
            model_name='articulos',
            name='familia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.familia'),
        ),
        migrations.AddField(
            model_name='articulos',
            name='impuesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.impuestos'),
        ),
        migrations.AddField(
            model_name='articulos',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.proveedores'),
        ),
        migrations.AddField(
            model_name='articulos',
            name='ubicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ubicaciones'),
        ),
        migrations.AddField(
            model_name='remision_prov',
            name='factura_proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.compra_prov'),
        ),
        migrations.AddField(
            model_name='remision_clie',
            name='factura_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.factura_clie'),
        ),
        migrations.AddField(
            model_name='factura_linea_clie',
            name='factura_cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.factura_clie'),
        ),
        migrations.AddField(
            model_name='compra_prov',
            name='codprov',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.proveedores'),
        ),
        migrations.AddField(
            model_name='compra_linea_prov',
            name='compra_cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.compra_prov'),
        ),
        migrations.CreateModel(
            name='Caja_tipo_pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_tipo_pago', models.FloatField(null=True)),
                ('caja_diaria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.caja_diaria')),
                ('tipo_pago', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.formapago')),
                ('compra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.compra_prov')),
                ('venta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.factura_clie')),
            ],
        ),
    ]
