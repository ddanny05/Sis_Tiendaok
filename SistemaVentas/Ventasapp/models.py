from typing import Any
from django.db import models
from .choices import CATEGORIAS,METODOS_PAGO
from decimal import Decimal
from django.core.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator, MinLengthValidator
from .validadores import validacion_numeros, Validacion_letras, validacion_especial,validacion_especial2,validacion_especial3

# Create your models here.
class Clientes(models.Model):
    cedula = models.CharField(primary_key=True, max_length=10, unique=True, validators=[MinLengthValidator(10)])
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    direccion = models.TextField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Productos(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10, unique=True)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_stock = models.PositiveIntegerField()
    fecha_elaboracion = models.DateField()
    fecha_vencimiento = models.DateField()
    def clean(self):
        if self.fecha_elaboracion >= self.fecha_vencimiento:
            raise ValidationError('La fecha de elaboración no puede ser igual o mayor que la de vencimiento.')
        diferencia_fechas = relativedelta(self.fecha_vencimiento, self.fecha_elaboracion)
        if diferencia_fechas.years >= 5:
            raise ValidationError('La fecha de vencimiento no puede superar los 5 años desde la elaboración.')
    def actualizar_stock(self, cantidad):
        if self.cantidad_stock < cantidad:
            raise ValidationError('Stock insuficiente para realizar esta operación.')
        self.cantidad_stock -= cantidad
        self.save()

    def sumar_stock(self, cantidad):
        self.cantidad_stock += cantidad
        self.save()

    def __str__(self):
        return f"{self.nombre}  {self.marca} "
    class Meta:
        verbose_name = 'Producto :'
        verbose_name_plural = 'Productos'
        db_table = 'Productos'

class Empresas (models.Model):
    ruc = models.CharField(primary_key=True, max_length=13, unique=True)
    nombre = models.CharField(max_length=50, blank=False, verbose_name='Nombre de la empresa : ')
    direccion = models.TextField()
    telefono = models.CharField(max_length=10)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} "
    class Meta:
        verbose_name = 'Empresa :'
        verbose_name_plural = 'Empresas'
        db_table = 'Empresas'

class Proveedores (models.Model):
    cedula = models.CharField(primary_key=True, max_length=10, unique=True, validators=[MinLengthValidator(10),validacion_numeros])
    nombre = models.CharField(max_length=50, blank=False, verbose_name='Nombre del proveedor : ')
    apellido = models.CharField(max_length=50, blank=False)
    telefono = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    empresa = models.ForeignKey(Empresas, on_delete= models.CASCADE)
    def __str__(self):
        return f"{self.nombre} ' ' {self.apellido} "
    class Meta:
        verbose_name = 'Proveedor '
        verbose_name_plural = 'Proveedores'
        db_table = 'Proveedores'

class Empleados (models.Model):
    cedula = models.CharField(primary_key=True, max_length=10, unique=True, verbose_name= 'Cedula del Empleado :',validators=[MinLengthValidator(10)])
    nombre = models.CharField(max_length=50, blank=False, verbose_name='Nombre del Empleado : ')
    apellido = models.CharField(max_length=50, blank=False)
    telefono = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    direccion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_nacimiento = models.DateField()
    def __str__(self):
        return f"{self.nombre} ' ' {self.apellido} "
    class Meta:
        verbose_name = 'Empleado :'
        verbose_name_plural = 'Empleados'
        db_table = 'Empleados'

class MetodoPago(models.Model):
    nombre = models.CharField(max_length=50, choices=METODOS_PAGO, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Método de Pago'
        verbose_name_plural = 'Métodos de Pago'

class Factura(models.Model):
    codigo_factura = models.AutoField(primary_key=True)
    fecha_factura = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.SET_NULL, null=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2,  default=0)
    iva = models.DecimalField(max_digits=10, decimal_places=2,  default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2,  default=0)
    def calcular_totales(self):
        """Calcula el subtotal, IVA (15%) y total de la factura."""
        self.subtotal = sum(detalle.subtotal for detalle in self.detallefactura_set.all())
        self.iva = self.subtotal * Decimal(0.15)
        self.total = self.subtotal + self.iva
        self.save()
    def __str__(self):
        return f"Factura {self.codigo_factura} - Cliente: {self.cliente.nombre}"

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'


class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2,  default=0)
    
    
    VENDIDA = "V"
    ANULADA = "A"

    ESTADOS = [
    (VENDIDA, "Vendida"),
    (ANULADA, "Anulada"), 
    ]
    estados = models.CharField(max_length=40, choices=ESTADOS)


        
    def calcular_subtotal(self):
        return self.cantidad * self.producto.precio

    def save(self, *args, **kwargs):
        """ Sobrescribe el método save para calcular valores automáticamente y manejar stock """
        self.subtotal = self.calcular_subtotal()  # Calcula el subtotal de manera controlada
        if self.estados == self.VENDIDA:
            self.producto.actualizar_stock(self.cantidad)
        elif self.estados == self.ANULADA:
            self.producto.sumar_stock(self.cantidad)
        super().save(*args, **kwargs)

            # Llamar al método calcular_totales para actualizar los totales de la factura
        self.factura.calcular_totales()
        
    
    def __str__(self):
        return f"Detalle de {self.factura} - Producto: {self.producto.nombre}"

    class Meta:
        verbose_name = 'Detalle Factura'
        verbose_name_plural = 'Detalles Facturas'
        db_table = 'DetallesFacturas'






