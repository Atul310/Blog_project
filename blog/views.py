from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Post # . operator use to import from current directory 
# models is the directory and we import Post
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                  DetailView ,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )
from datetime import datetime
from .forms import Comment,CommentForm
from django.contrib.auth.decorators import login_required
# from .forms import CommentForm
# this render helps to point to the template and return whenever 
# to naviagtese) particular page.
# Create your views here.    
# posts 

def index(request):
    return render(request,'blog/index.html')

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
    paginate_by=4

class UserPostListView(ListView):
    model=Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    
class PostDetailView(DetailView):
    model = Post

    template_name = 'blog/post_detail.html'




#    

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']
    success_url='/Blog/home'
    def form_valid(self,form):
        form.instance.author =self.request.user
        return super().form_valid(form)
    


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']
    success_url='/Blog/home'
    
    def form_valid(self,form):
        form.instance.author =self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False 
        

    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url= '/Blog/home'
    def test_func(self):
        post=self.get_object()
        if self.request.user== post.author:
            return True
        return False
    
        

def sidebar_view(request):
    current_datetime = datetime.now()
    context = {'current_date': current_datetime}
    return render(request, 'base.html', context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})

def my_blogs(request):
    
    if request.user.is_authenticated:
        # Filter blogs by the logged-in user
        user_blogs = Post.objects.filter(author=request.user)
        blogs_per_page = 5  # You can adjust this value based on your preferences

        # Create a Paginator object
        paginator = Paginator(user_blogs, blogs_per_page)
         # Get the current page number from the request's GET parameters
        page_number = request.GET.get('page')

        # Get the Page object for the current page
        blogs_page = paginator.get_page(page_number)

        context = {'user_blogs': blogs_page}  # Use a different variable name, e.g., 'blogs_page'
        return render(request, 'blog/my_blogs.html', context)
    else:
         # Handle the case when the user is not logged in
        return render(request, 'blog/my_blogs.html')

def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('blog/home')  # Redirect to the blog home page after comment submission

    return redirect('blog-home')  # Handle GET requests or form validation errors by redirecting to the blog home page

@login_required  # Use the login_required decorator for replying to comments as well
def reply_comment(request, post_id, parent_id):
    post = get_object_or_404(Post, id=post_id)
    parent_comment = get_object_or_404(Comment, id=parent_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.parent = parent_comment
            comment.save()
            return redirect('blog-home')  # Redirect to the blog home page after reply submission

    return redirect('blog-home')  # Handle GET requests or form validation errors by redirecting to the blog home page
