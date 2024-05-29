from django.shortcuts import render
from myapp.models import Blog

def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})
    
def about(request):
    return render(request,'about.html')
def blog(request):
    #  Retrieve all blog posts from the database
 blogs = Blog.objects.all()
 return render(request, 'blog.html', {'blogs': blogs})
  
def contact(request):
    return render(request, 'contact.html')
def single(request):
    #  Retrieve all blog posts from the database
 blogs = Blog.objects.all()
 return render(request, 'single.html', {'blogs': blogs})

# def blog_list(request):
#     # Retrieve all blog posts from the database
#     blogs = Blog.objects.all()
#     return render(request, 'blog.html', {'blogs': blogs})
