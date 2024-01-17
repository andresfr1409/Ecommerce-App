from django.db import models
from django.contrib.auth.models import User
from django.db.models import F, Sum, FloatField
from Tienda.models import Producto
class Pedido(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        
        return f'Pedido #{self.id} - {self.user_id.username}' 
    
    @property
    def total(self):
        
        return self.lineapedido_set.aggregate(
            
            total = Sum(F("precio")*F("cantidad"), output_field = FloatField())
        
        )["total"]
    
    class Meta:
        db_table = 'Pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']

class LineaPedido(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    creado = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        
        return f'Linea de pedido#{self.id} - {self.cantidad} unidad/s de {self.producto_id.nombre}'
    class Meta:
        db_table = 'LineaPedidos'
        verbose_name = 'LineaPedido'
        verbose_name_plural = 'LineaPedidos'
        ordering = ['id']