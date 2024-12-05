from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from .models import Clientes,Empleados,Factura,Productos,Proveedores,Empresas,DetalleFactura,MetodoPago
# Register your models here.

#Uso de decoradores para mejorar la presentacion en el panel de admin
@admin.register (Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'telefono', 'direccion', 'email')
    search_fields = ('cedula', 'nombre', 'apellido')
    list_filter = ('cedula', 'apellido')
    
@admin.register (Empleados)
class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'telefono', 'direccion', 'email')
    search_fields = ('cedula', 'nombre', 'apellido')
    list_filter = ('cedula', 'apellido')

@admin.register (Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('codigo_factura','fecha_factura','cliente','subtotal', 'iva', 'total')
    
    #para hacer que atributo no pueda modificarse
    """def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['codigo_factura','fecha_factura','producto' ]
        return [] """
   #restriccion para poder borrar un registro cumple la misma funcion que cuando lo hacemos desde permisos de ususarios (delete)
    #def has_delete_permission(self, request, obj=None ):  #obj=None hace referencia a la instacia (objeto del modelo), NONE = quiere decir el objeto aun no existe
        #return True
    
@admin.register (Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('nombre','cantidad_stock')

admin.site.register (MetodoPago)
class MetodoAdmin(admin.ModelAdmin):
    list_display = ('nombre','tipo')

@admin.register(DetalleFactura)
class DetalleFacturaAdmin(admin.ModelAdmin):
    list_display = ('factura', 'producto', 'cantidad', 'subtotal')
   
        
@admin.register (Proveedores)
class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('cedula','nombre','apellido') 
    
@admin.register (Empresas)
class EmpresasAdmin(admin.ModelAdmin):
    list_display = ('ruc','nombre','telefono')  



    
    