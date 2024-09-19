from     django.urls import  path
from .views import *


urlpatterns=[
    path("",index,name="index"),
    path("page/<int:pagenumber>",index,name="page"),
    path("blog/<int:id>",blog,name="blog"),
    path("contact",contact,name="contact"),
    path("category/<int:cat>/", index, name="category"),

]
