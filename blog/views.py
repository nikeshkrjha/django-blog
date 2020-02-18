from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

posts = Post.objects.all()

def home(request):
    context = {'posts': posts}
    print(context)
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'Blog Demo'})

def portfolio(request):
    return render(request, 'blog/portfolio.html', {'title': 'Blog Portfolio'})


### Class based views #####
class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

