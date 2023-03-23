from django.contrib import admin
from .models import Blog_model,Profile_model
# Register your models here.

admin.site.register(Blog_model)
admin.site.register(Profile_model)