from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from CarroCompras.carro import Carro
from Pedidos.models import Pedido,LineaPedido

@login_required
def procesar_compra(request):
    
    pedido = Pedido.objects.create(user = request.user)
    carro = Carro(request)
    lineas_pedido = list()
    for key,value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            
            producto_id = key,
            cantidad = value["cantidad"],
            user = request.user,
            pedido = pedido
        ))
    
    LineaPedido.objects.bulk_create(lineas_pedido)
    
    '''
    enviar_mail(
        pedido = pedido,
        lineas_pedido = lineas_pedido,
        nombre_usuario = request.username,
        email_usuario = request.usermail,
    )
    '''
    messages.success(request, "Compra realizada exitosamente")
    
    return redirect('Tienda')
