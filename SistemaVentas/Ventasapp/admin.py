from django.contrib import admin
from .models import Clientes,Empleados,Factura,Productos,Proveedores,Empresas
# Register your models here.

admin.site.register (Empleados)
admin.site.register (Factura)
admin.site.register (Proveedores)
admin.site.register (Empresas)

#Uso de decoradores para mejorar la presentacion en el panel de admin
@admin.register (Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'telefono', 'direccion', 'email')
    search_fields = ('cedula', 'nombre', 'apellido')
    list_filter = ('cedula', 'apellido')

@admin.register (Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('nombre','cantidad_stock')
    