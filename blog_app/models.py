from django.db import models
from froala_editor.fields import FroalaField
from .helpers import *
from django.contrib.auth.models import User



class Profile_model(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_varified = models.BooleanField(default=False)
    token = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.user.username

class Blog_model(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = FroalaField(theme='dark')
    post = models.ImageField(upload_to="blogpost")
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=1000,null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        #sending it to helper function to generate slug
        self.slug = generating_slug(self.title)
        #super is used to override the buildin
        super(Blog_model,self).save(*args,**kwargs)
