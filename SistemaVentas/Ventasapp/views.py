from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClientesSerializer
from .models import Clientes, Productos, Proveedores

# Create your views here.
# las vistas sirven para poder acceder a los metodos que ofrece una api (metodos POST, GET, PUT, DELETE)
#POST: para enviar informacion.(utilizado en los formularios para enviar informacion)
# GET: para enviar/obtener informacion
#PUT: para actualizar informacion
#DELETE: para borrar informacion

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all() #queryset para visualizar los registros en formato json #object indica los objetos del modelo clinets, all trae a todos los objetos 
    serializer_class = ClientesSerializer #el serializares class indica cual es el que va a utilizar la vista.
    