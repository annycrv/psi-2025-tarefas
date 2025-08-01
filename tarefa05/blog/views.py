from django.shortcuts import render
from .models import Postagem, Blog


def index(request):
    context = {
        "postagens": Postagem.objects.all(),
        "blog": Blog.objects.first(),
    }
    return render(request, 'blog/index.html', context)

def post(request, id_post):
    context = {
        "post": Postagem.objects.all(),
        "blog": Blog.objects.first(),
    }
    return render(request, "blog/post.html", post[id_post-1])