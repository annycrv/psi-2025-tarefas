from django.shortcuts import render, get_object_or_404
from .models import Postagem, Blog


def index(request):
    context = {
        "postagens": Postagem.objects.all(),
        "blog": Blog.objects.first(),
    }
    return render(request, 'blog/index.html', context)

def post(request, id_post):
    postagem = get_object_or_404(Postagem, id=id_post)
    context = {
        "post": postagem,
        "blog": Blog.objects.first(),
    }
    return render(request, "blog/post.html", context)