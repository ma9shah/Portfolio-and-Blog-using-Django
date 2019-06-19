
# from django.contrib import admin
from . import views
from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('<int:blog_id>', views.own_blog, name='own_blog'),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
