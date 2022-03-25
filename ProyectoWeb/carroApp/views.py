from django.shortcuts import render
from .carro import Carro
from tiendaApp.models import Producto
from django.shortcuts import redirect
# Create your views here.

def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar_producto(producto=producto)
    return redirect("tiendaApp")

def eliminar_prodto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar_producto(producto=producto)
    return redirect("tiendaApp")

def restar_prodto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("tiendaApp")

def limpiar_carro(request, producto_id):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("tiendaApp")