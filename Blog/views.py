from django.shortcuts import render, get_object_or_404
from Blog.models import Post, Categoria

def blog(request):
    
    posts = Post.objects.all()
    categorias = Categoria.objects.all()
    
    return render(request,'blog/blog.html',{'posts': posts, 'categorias': categorias})

def categoria(request, categoria_id):
    categorias = Categoria.objects.all()
    # Se obtiene la categoría específica o retorna un error 404 si no existe
    categoria = get_object_or_404(Categoria, id=categoria_id)
    # Se obtienen los posts asociados a la categoría
    posts = Post.objects.filter(categorias=categoria)
    # Se pasa la categoría y los posts al template como contexto
    return render(request, 'blog/categorias.html', {'categorias': categorias,'categoria': categoria, 'posts': posts})