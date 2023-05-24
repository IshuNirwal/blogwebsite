from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.urls import *

# Create your models here.

#Category model

class Category(models.Model):
    title=models.CharField(max_length=100)
    cat_id=models.AutoField(primary_key=True)
    description=models.CharField(max_length=300)
    url=models.CharField(max_length=100)
    image=models.ImageField(upload_to='category/')
    add_date=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
       return f"{self.title}"
    def image_tag(self):
       return format_html('<img src="/media/{}" style="width:40px;height:40px"  />'.format(self.image))
    
# Post model

class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=HTMLField()
    url=models.CharField(max_length=100)
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='post/')
    def __str__(self):
        return f"{self.title}"
    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px"  />'.format(self.image))
    
class ContactEnquiry(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    message=models.TextField()
    def __str__(self):
        return f"{self.name}"
    
class HandleRequest(models.Model):
    name=models.CharField(max_length=100)
    cardnumber=models.IntegerField()
    date1=models.IntegerField()
    date2=models.IntegerField()
    cvc=models.IntegerField()
    def __str__(self):
        return f"{self.name}"
    
class Comment(models.Model):
    name=models.CharField(max_length=100,default="")
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments',default="",null=True)
    comment=models.TextField(max_length=200,default="")
    date=models.DateTimeField(auto_now=True,null=True)
    email=models.EmailField()
    def __str__(self):
        return f"{self.name}"
    


    