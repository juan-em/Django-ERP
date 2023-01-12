# Generated by Django 3.2 on 2023-01-12 13:17

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
                ('referencia', models.CharField(max_length=20)),
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
                ('precio_almacen', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('precio_tienda', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('precio_con_iva', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('imagen', models.ImageField(null=True, upload_to=app.models.upload_path)),
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
                ('borrado', models.CharField(default=0, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('iva', models.IntegerField()),
                ('totalfactura', models.FloatField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('borrado', models.CharField(default=0, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Formapago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrefp', models.CharField(max_length=100)),
                ('borrado', models.CharField(default=0, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Impuestos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('valor', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('borrado', models.CharField(default=0, max_length=1)),
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
            name='Provincias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreprovincia', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ubicaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('borrado', models.CharField(default=0, max_length=1)),
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
            name='Factura_clie',
            fields=[
                ('factura', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.factura')),
                ('codcliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.clientes')),
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
        migrations.AddField(
            model_name='persona',
            name='codprovincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.provincias'),
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
                ('factura_cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.factura_clie')),
            ],
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
        migrations.CreateModel(
            name='Albaran_linea_clie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcionproducto', models.TextField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.factura_linea_clie')),
            ],
        ),
    ]
