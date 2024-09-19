from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *
from taggit.models import Tag

# Create your views here.


def index(request,cat=None,pagenumber=1):
    if request.method=="GET":
        stories=Story.objects.all()
        if cat:
            posts=Post.objects.all().filter(category__id=cat)
        else:
            posts=Post.objects.all()
        posts_ordered_cv=Post.objects.all().order_by('counted_views')
        posts_ordered_pd=Post.objects.all().order_by('published_date')
        posts_slider=Post_Slider.objects.all()
        categories=Category.objects.all()
        tags=Tag.objects.all()

        paginator = Paginator(posts, 2)  # Show 25 contacts per page.
        page_obj = paginator.get_page(pagenumber)


        context={"stories":stories,
                 "posts":page_obj,
                 "posts_slider_ordered":posts_ordered_cv,
                 "posts_ordered":posts_ordered_pd,
                 "posts_slider":posts_slider,
                 "categories":categories,
                 "tags":tags,
                 "page_obj":page_obj,
                 "paginator":paginator}

        return render(request,"index.html",context)





def blog(request,id):
    post=Post.objects.filter(id=id).get()
    previous_post=Post.objects.exclude(id__gte=id).last()
    next_post=Post.objects.exclude(id__lte=id).first()

    post.counted_views+=1
    post.save()


    context={'post':post,"previous_post":previous_post,"next_post":next_post}

    return render(request,"blog-details.html",context)


def contact(request):
    return render(request,"contact.html")


