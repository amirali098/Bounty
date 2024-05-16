from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    stories=Story.objects.all()
    posts=Post.objects.all()
    posts_ordered_cv=Post.objects.all().order_by('counted_views')
    posts_ordered_pd=Post.objects.all().order_by('published_date')
    posts_slider=Post_Slider.objects.all()

    context={"stories":stories,
             "posts":posts,
             "posts_slider_ordered":posts_ordered_cv,
             "posts_ordered":posts_ordered_pd,
             "posts_slider":posts_slider}

    return render(request,"index.html",context)



def category(request):
    return render(request,"category.html")


def archive(request):
    return render(request,"archive.html")


def blog(request):
    return render(request,"blog.html")


def contact(request):
    return render(request,"contact.html")


