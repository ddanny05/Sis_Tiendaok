#los serializadores convierten los registros en formato json (clave, valor) formato de diccionarios pero en json
from rest_framework import serializers
from .models import Clientes,Empleados,Factura,Productos,Proveedores,Empresas

#Serializador para Clientes
#vamos a convertir los registros en formato json (clave, valor) formato de diccionarios
class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = ['cedula', 'nombre', 'apellido', 'telefono', 'email','direccion', 'fecha_creacion', 'fecha_nacimiento']
        #fields = '__all__'