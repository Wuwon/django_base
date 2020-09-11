from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
# Create your views here.

def index(request):
    post = Post.objects.all()

    context={
        'post' : post
    }

    return render(request,'index.html',context)


def detail(request,post_id):
    post = Post.objects.get(pk=post_id)

    context={
        'post' : post
    }

    return render(request,'detail.html',context)

def new(request):
    return render(request,'new.html')

def create(request):
    author = request.POST['author']
    subject = request.POST['subject']
    body = request.POST['body']
    image = None

    post = Post(author=author,subject=subject,body=body,image=image,create_time=timezone.now())
    post.save()
    
    return redirect('detail', post_id=post.pk)

def edit(request,post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'post' : post
    }
    return render(request,'edit.html',context)


def update(request,post_id):
        post = Post.objects.get(pk=post_id)
        subject = request.POST["subject"]
        body = request.POST['body']
        image = None
        post = Post(subject=subject,body=body,image=image,create_time=timezone.now())
        post.save()

        return redirect('detail', post_id=post.pk)

def delete(request,post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('index')