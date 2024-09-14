from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from rest_framework import viewsets
from .serializer import BlogSerializer
from .models import Blog
# Create your views here.
class BlogListview(ListView):
    model = Blog
    fields = [
        'topic',
        'body'
    ]
    template_name = 'cocoaApp/list.html'
    
class BlogCreateview(CreateView):
    model = Blog
    fields = ['topic','body']
    template_name = 'cocoaApp/newpost.html'
    success_url = '/'
    
class BlogDeleteview(DeleteView):
    model = Blog
    template_name = 'cocoaApp/delete.html'
    success_url = '/'
class BlogUpdateview(UpdateView):
    model = Blog
    fields = '__all__'
    template_name = 'cocoaApp/newpost.html'
    success_url = '/'
    
class BlogViewset(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer