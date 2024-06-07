from django.shortcuts import render
from myapp.models import Blog
from myapp.forms import SearchForm

def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})
    
def about(request):
    return render(request,'about.html')
def blog(request):
 blogs = Blog.objects.all()
 return render(request, 'blog.html', {'blogs': blogs})
  
def contact(request):
    return render(request, 'contact.html')
def single(request):
   
 blogs = Blog.objects.all()
 return render(request, 'single.html', {'blogs': blogs})

# def blog_list(request):
#     # Retrieve all blog posts from the database
#     blogs = Blog.objects.all()
#     return render(request, 'blog.html', {'blogs': blogs})

def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            results = Blog.objects.filter(title__icontains=query)
            return render(request, 'search_results.html', {'results': results, 'query': query})
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})
