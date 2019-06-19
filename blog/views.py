from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_home(req):
    blogs=Blog.objects.all
    return render(req, 'blog.html', {'blogs':blogs})
def own_blog(req, blog_id):
    current_blog= get_object_or_404(Blog, pk=blog_id)
    return render(req, 'own_blog.html', {'own_blog':current_blog})
