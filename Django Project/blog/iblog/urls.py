from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home,name='home'),
    path('blog/<slug:url>', post),
    path('category/<slug:url>', category),
    path('contact/',contact),
    path('email/',contact),
    path('search',search,name='search'),
    path('handlerequest/',handlerequest,name='handlerequest'),
    path('',sign),
    path('signup/',signup),
    path('about/',About)
   
]
