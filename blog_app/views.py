from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout
# Create your views here.
from .forms import Blog_model_form
from .models import Blog_model,Profile_model

def index_view(request):
    #now printing all small chunks of blogs present in data base
    context = {"blogs": Blog_model.objects.all()}
    return render(request,"index.html",context)

def login_view(request):
    return render(request,"login.html")

def logout_view(request):
    logout(request)
    return redirect("index")

def register_view(request):
    return render(request,"register.html")


def add_block_view(request):

    context = {"form": Blog_model_form}
    try:
        if request.method == "POST":
            form = Blog_model_form(request.POST) #only context part will be save throug form
            image = request.FILES['image']
            title = request.POST.get('title')
            author = request.POST.get('author')
            # this is for the login user
            user = request.user
            print(user)
            if form.is_valid():
                content = form.cleaned_data['content'] #if valid now add into conent
            
            # creating obj to store into database
            blog_obj = Blog_model.objects.create(
                user = user ,title = title,content = content, post=image,author=author)
            print(blog_obj)
            blog_obj.save()
            

    except Exception as e:
        print(e)
    return render(request,"add_blog.html",context)


def show_detial_view(request,slug):
    context = {}
    try:
        blog_obj = Blog_model.objects.filter(slug=slug).first()
        print(blog_obj.title)
        context ['blog']= blog_obj
    except Exception as e:
        print(e)
    return render(request,'details.html',context)

def my_blog_view(request):
    context = {}
    try:
        user_obj = Blog_model.objects.filter(user=request.user)
        context["user_obj"] = user_obj
    except Exception as e:
        print(e)
    return render(request,"my_blogs.html",context)


def edit_blog_view(request,slug):
    context = {}
    try:
        user_obj = Blog_model.objects.get(slug=slug)
        if request.user != user_obj.user:
            return redirect("")
            # puting inital value into model form other values can be directly inserted
        initial_dic = {"content": user_obj.content}
        form = Blog_model_form(initial=initial_dic)
    
        context["user_obj"] = user_obj
        context["form"] = form
        
        if request.method == "POST":
            form = Blog_model_form(request.POST) #only context part will be save throug form
            image = request.FILES['image']
            title = request.POST.get('title')
            author = request.POST.get('author')
            # this is for the login user

            blog_obj = Blog_model.objects.filter(slug=slug).first()
            user = request.user
            
            print(user)
            if form.is_valid():
                content = form.cleaned_data['content'] #if valid now add into conent
                blog_obj.title = title
                blog_obj.author = author
                blog_obj.content= content
                blog_obj.post = image
                blog_obj.save()
            
            # creating obj to store into database
            return redirect("my_blogs")
    except Exception as e:
        print(e)
    return render(request,"edit_blog.html",context)

def delete_blog_view(request,id):
    try:
        user_obj = Blog_model.objects.get(id=id)
        if user_obj.user == request.user:
            user_obj.delete()
            return redirect("my_blogs")
    except Exception as e:
        print(e)
    return render(request,"delete_blog.html")


def verify_view(request,token):
    try:
        user_obj = Profile_model.objects.filter(token=token).first()

        if user_obj:
            user_obj.is_varified = True
            user_obj.save()

    except Exception as e:
        print(e)
    return redirect("/login/")


def error_404_view(request,exception):
    return render(request,'404.html')