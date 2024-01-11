from django.db import models

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'categoriaProducto'
        verbose_name_plural = 'categoriasProductos'
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=150)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='tienda')
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now_add=True)  
    
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        
    def __str__(self):
        return self.nombre