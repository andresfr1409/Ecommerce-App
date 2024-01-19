from django.urls import path
from PedidosTienda import views

urlpatterns = [
    path('',views.procesar_compra,name='procesar_compra'),
]
