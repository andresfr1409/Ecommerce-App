from django.urls import path
from Pedidos import views

urlpatterns = [
    path('',views.procesar_compra,name='procesar_compra'),
]
