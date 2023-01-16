from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Provincias(models.Model):
    nombreprovincia = models.CharField(max_length=100)
    def __str__(self):
        return self.nombreprovincia

class Formapago(models.Model):
    nombrefp = models.CharField(max_length=100)
    def __str__(self):
        return self.nombrefp

class Entidades(models.Model):
    nombreentidad = models.CharField(max_length=100)
    def __str__(self):
        return self.nombreentidad

class Familia(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=100)
    codprovincia = models.ForeignKey(Provincias, on_delete=models.CASCADE)
    localidad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=500)
    codpostal = models.CharField(max_length=100)
    cuentabancaria = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    movil = models.CharField(max_length=100)
    web = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    estructurajuridica = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    codprovincia = models.ForeignKey(Provincias, on_delete=models.CASCADE)
    localidad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=500)
    codpostal = models.CharField(max_length=100)
    cuentabancaria = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    movil = models.CharField(max_length=100)
    web = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Clientes(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, primary_key=True)
    codformapago = models.ForeignKey(Formapago, on_delete=models.CASCADE)
    borrado = models.CharField(max_length=1, default=0)

    def __str__(self):
        return self.persona.nombre

class Proveedores(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)
    ruc = models.CharField(max_length=100)
    borrado = models.CharField(max_length=1, default=0)

    def __str__(self):
        # return self.persona.nombre
        if self.persona:
            prov = f'{self.persona}'
        else:
            prov = f'{self.empresa}'
        return prov

CHOICES = (("1", "1"),
    ("0", "0"))
def upload_path(instance, filename):
    return '/'.join(['articulos',str(instance.referencia),filename])

class Ubicaciones(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Impuestos(models.Model):
    nombre = models.CharField(max_length=100)
    valor = models.FloatField(validators=[MinValueValidator(0.0)])
    def __str__(self):
        return self.nombre

class Embalajes(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

CHOICES_YES_NO = (("Sí", "Sí"),
    ("No", "No"))

class Articulos(models.Model):
    #cambiar luego por nombre
    referencia = models.CharField(max_length=20)
    familia = models.ForeignKey(Familia,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=500)
    impuesto = models.ForeignKey(Impuestos, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    descripcion_corta = models.CharField(max_length=100)
    ubicacion = models.ForeignKey(Ubicaciones, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    stock_minimo = models.PositiveIntegerField()
    aviso_minimo = models.CharField(max_length=3,choices=CHOICES_YES_NO)
    datos_producto = models.CharField(max_length=500)
    fecha_alta = models.DateTimeField()
    embalaje = models.ForeignKey(Embalajes, on_delete=models.CASCADE)
    unidades_por_caja = models.PositiveIntegerField()
    observaciones = models.CharField(max_length=500)
    precio_compra = models.FloatField(validators=[MinValueValidator(0.0)])
    precio_almacen = models.FloatField(validators=[MinValueValidator(0.0)])
    precio_tienda = models.FloatField(validators=[MinValueValidator(0.0)])
    precio_con_iva = models.FloatField(validators=[MinValueValidator(0.0)])
    imagen = models.ImageField(upload_to=upload_path, null=True)
    def __str__(self):
        return self.referencia

#Facturas

class Factura(models.Model):
    fecha = models.DateField(null=True)
    iva = models.IntegerField()
    totalfactura = models.FloatField(default=0, null=True)    
    
class Factura_clie(models.Model):
    factura = models.OneToOneField(Factura, on_delete=models.CASCADE, primary_key=True)
    codcliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)

    def __str__(self):
        return "Nombre cliente:{}, Cod. Factura:{}".format(self.codcliente.persona.nombre, self.factura.pk)

class Factura_linea_clie(models.Model):
    factura_cliente = models.ForeignKey(Factura_clie, on_delete=models.CASCADE, null=True)
    codproducto = models.ForeignKey(Articulos, on_delete=models.CASCADE, null=True)
    cantidad = models.IntegerField()
    precio = models.FloatField()
    importe = models.FloatField(null=True)
    dsctoproducto = models.FloatField()

    def __str__(self):
        return "Nombre articulo:{}".format(self.codproducto.referencia)

#Compras a Proveedores
def upload_path2(instance, filename):
    return '/'.join(['Compras',str(instance.compra),filename])
class Compra_prov(models.Model):
    compra = models.OneToOneField(Factura, on_delete=models.CASCADE, primary_key=True)
    codprov = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    imagen_factura_compra = models.ImageField(upload_to=upload_path2, null=True)

    def __str__(self):
        if self.codprov.persona:
            compra_prov = "Nombre proveedor:{}, Cod. Compra:{}".format(self.codprov.persona.nombre, self.compra.pk)
        else:
            compra_prov = "Nombre proveedor:{}, Cod. Compra:{}".format(self.codprov.empresa.nombre, self.compra.pk)
        return compra_prov

class Compra_linea_prov(models.Model):
    compra_cliente = models.ForeignKey(Compra_prov, on_delete=models.CASCADE, null=True)
    codproducto = models.ForeignKey(Articulos, on_delete=models.CASCADE, null=True)
    cantidad = models.IntegerField()
    precio = models.FloatField()
    importe = models.FloatField(null=True)
    dsctoproducto = models.FloatField()

    def __str__(self):
        return "Nombre articulo:{}".format(self.codproducto.referencia)

######################
#Albaranes Prueba
class Remision_clie(models.Model):
    factura_cliente = models.ForeignKey(Factura_clie, on_delete=models.CASCADE)

    def __str__(self):
        return "Numero de linea:{}".format(self.factura.numlinea)

#Albaranes Linea intermedia Prueba
class Remision_linea_clie(models.Model):
    codremision = models.ForeignKey(Remision_clie, on_delete=models.CASCADE)
    codproducto = models.ForeignKey(Factura_linea_clie, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "Numero de remisión:{}".format(self.codremision.pk)