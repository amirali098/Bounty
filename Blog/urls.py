from     django.urls import  path
from .views import *


urlpatterns=[
    path("",index,name="index"),
    path("category",category,name="category"),
    path("archive",archive,name="archive"),
    path("blog",blog,name="blog"),
    path("contact",contact,name="contact"),
]
