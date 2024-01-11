from django.urls import path
from CarroCompras import views 

urlpatterns = [
    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar_producto'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('sumar/<int:producto_id>/', views.sumar_producto, name='sumar_producto'),
    path('restar/<int:producto_id>/', views.restar_producto, name='restar_producto'),
    path('vaciar/', views.vaciar_carrito, name='vaciar_carrito'),
    path('carrito/', views.carrito, name='carrito'),
    path('producto_agregado/<int:producto_id>/', views.producto_agregado, name='producto_agregado'),
]
