
from .models import Post # . operator use to import from current directory 
# models is the directory and we import Post
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (ListView,
                                  DetailView ,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )

# this render helps to point to the template and return whenever 
# to naviagtese) particular page.
# Create your views here.    
# posts 

def home(request):
   
    context ={
        'posts':Post.objects.all() #posts
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name ='posts'
    ordering = ['-date_posted']
    
class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']
    def form_valid(self,form):
        form.instance.author =self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']
    def form_valid(self,form):
        form.instance.author =self.request.user
        return super().form_valid(form)
    def test_form(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False 

    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url= '/'

def about(request):
    return render(request,'blog/about.html',{"titl]e":"About"})
