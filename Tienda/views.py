from django.shortcuts import render
from Tienda.models import CategoriaProducto, Producto

def tienda(request):
    
    productos = Producto.objects.all()
    
    categoriasP = CategoriaProducto.objects.all()
    
    
    return render(request,'tienda/tienda.html', {'productos': productos, 'categoriasP': categoriasP})
