from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.http import HttpResponse
from .models import *
from django.shortcuts import get_object_or_404


class AuthorList(ListView):
    model=Author
    context_object_name='Author'
    template_name='news/author_list.html'

class PostList(ListView):
    model = Post
    context_object_name = 'Post'
    template_name = 'default.html'
    ordering = '-date'

class Post(DetailView):
    model = Post
    context_object_name = 'Post'



def index(request):
    news= New.objects.all()
    return render(request,'index.html',context={'news':news})

def default(request,slug):
    new=New.objects.get(slug__iexact=slug)
    return render(request,'default.html',context={'new':new})

