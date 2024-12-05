"""
URL configuration for SistemaVentas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# creamos las rutas que van a utilizar las vistas

from django.contrib import admin
from django.urls import path, include  #include sierve para incluir las urls de una objeto
from Ventasapp.views import ClientesViewSet
from rest_framework.routers import DefaultRouter  #defaultrouter nos permite crear un objeto para acceder al metodo register que permite registar alas urls.

rutas= DefaultRouter()  #creamos un objetos a partir de la clase Defaultrouter
rutas.register('Clientes', ClientesViewSet) # el metodo registers necesita dos parametros 1. el nombre de la ruta, y la vista q va a utilizar esa ruta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(rutas.urls)) #creamos la ruta general de la api e incluimos a las urls del objetos rutas como parametro.
    
]

