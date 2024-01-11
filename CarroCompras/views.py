from django.shortcuts import redirect, render
from django.urls import reverse
from .carro import Carro
from Tienda.models import Producto

def agregar_producto(request, producto_id):
    
    producto = Producto.objects.get(id=producto_id)
    
    carro = Carro(request)
    carro.agregar(producto)
    
    return redirect(reverse('producto_agregado', kwargs={'producto_id': producto.id}))

def eliminar_producto(request, producto_id):
    
    producto = Producto.objects.get(id=producto_id)
    
    carro = Carro(request)
    carro.eliminar(producto)
    
    return redirect('carrito')

def restar_producto(request, producto_id):
    
    producto = Producto.objects.get(id=producto_id)
    
    carro = Carro(request)
    carro.restar(producto)
    
    return redirect('carrito')

def sumar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    
    carro = Carro(request)
    carro.agregar(producto)
    
    return redirect('carrito')

def vaciar_carrito(request):
    
    carro = Carro(request)
    carro.vaciar()
    
    return redirect('carrito')

def carrito(request):
    
    carro = Carro(request)
    
    return render(request, 'carro/carrito.html', {'carro': carro})

def producto_agregado(request, producto_id):
    
    producto = Producto.objects.get(id=producto_id)
    
    return render(request, 'carro/producto_agregado.html', {'producto': producto})
