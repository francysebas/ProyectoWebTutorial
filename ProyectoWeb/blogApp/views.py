from django.shortcuts import render
from django.shortcuts import render
from blogApp.models import Post, Categoria


# Create your views here.

def blog(request):
    posts = Post.objects.all()
    return render(request, "blogApp/blog.html", {"posts": posts})


# muestra en otra vista solo los filtros de las categorias
def categoria(request, categoria_id):
    categori = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categori)

    return render(request, "blogApp/categoria.html", {'categoria': categori, "posts": posts})
