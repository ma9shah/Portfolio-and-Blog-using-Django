from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_home(req):
    blogs=Blog.objects.all
    return render(req, 'blog.html', {'blogs':blogs})

def own_blog(req, title_url): #! 'title' comes from urls.py -> <str:title> 
    current_blog= get_object_or_404(Blog, title=title_url)
    return render(req, 'own_blog.html', {'own_blog':current_blog})
