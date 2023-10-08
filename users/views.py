from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required   # use of this is 
from django.contrib import messages 
from .forms import UserRegisterForm,UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView


# Create your views here.
def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')
            messages.success(request,f'Account created for !! You are able to login')
            return redirect('login')
              

    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method=='POST':
        u_form= UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
         u_form.save()
         p_form.save()
         messages.success(request,f'Your account has been updated')
         return redirect('profile')       
    else:
        u_form= UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        
        'u_form':u_form,
        'p_form':p_form
    }
    
    return render(request,'users/profile.html',context)

def user_profile(request,username):
    user= User.objects.get(username= username)
    return render (request, user)
    




class UserProfileDetailView(DetailView):
    model = User
    template_name = 'users/profile_detail.html'  # Create a template for displaying the user profile
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        return self.request.user








        
#  it add functionality to the existing function 
# it add funcutionality to our profile view where user must be logged in to  view this page
  
        
         
    
  
    # messages are imported from django for using flashing messages
    