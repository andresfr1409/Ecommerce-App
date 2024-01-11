from django.contrib import admin
from Blog.models import Categoria, Post

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created' , 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created' , 'updated')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
