from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    post = Post.objects.all()

    context={
        'post' : post
    }

    return render(request,'index.html',context)


def detail(request,post_id):
    post = Post.objects.get(id=post_id)

    context={
        'post' : post
    }

    return render(request,'detail.html',context)