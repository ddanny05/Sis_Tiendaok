#los serializadores convierten los registros en formato json (clave, valor) formato de diccionarios pero en json
from rest_framework import serializers
from .models import Clientes,Empleados,Factura,Productos,Proveedores,Empresas

#Serializador para Clientes
