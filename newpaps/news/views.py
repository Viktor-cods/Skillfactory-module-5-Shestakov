from django.shortcuts import render
from django.views.generic import (ListView,DetailView,CreateView,DeleteView,UpdateView)
from django.http import HttpResponse
from .models import *
from django.shortcuts import get_object_or_404
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy



class AuthorList(ListView):
    model=Author
    context_object_name='Author'
    template_name='news/author_list.html'


class PostList(ListView):
    model = Post
    context_object_name = 'Post'
    template_name = 'news/index.html'
    ordering = '-date'
    paginate_by= 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['time_now'] = datetime.utcnow()
        return context


def index(request):
    news= New.objects.all()
    return render(request,'index.html',context={'news':news})

def default(request,slug):
    new=New.objects.get(slug__iexact=slug)
    return render(request,'default.html',context={'new':new})


class PostDetail(DetailView):
    model = Post
    template_name='news/post.html'
    context_object_name = 'post'


class PostSearch(ListView):
    model = Post
    ordering = 'title'
    template_name = 'news/search.html'
    context_object_name = 'search'





class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news/post_edit.html'
    context_object_name = 'create'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.quantity = 10
        return super().form_valid(form)

class PostDelete(DeleteView):
    model = Post
    template_name = 'news/post_delete.html'
    success_url = reverse_lazy('post_edit')


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news/post_edit.html'
