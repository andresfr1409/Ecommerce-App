from django.contrib import admin
from Pedidos.models import Pedido,LineaPedido

class PedidoAdmin(admin.ModelAdmin):
    readonly_fields = ('creado',)

class LineaPedidoAdmin(admin.ModelAdmin):
    readonly_fields = ('creado',)

admin.site.register(Pedido, PedidoAdmin)
admin.site.register(LineaPedido, LineaPedidoAdmin)
