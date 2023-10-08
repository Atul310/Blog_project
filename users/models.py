from django.db import models
from django.contrib.auth.models import User
from PIL import Image 
from django.conf import settings
from django.shortcuts import get_object_or_404,render
# from .forms import ProfiledisplayForm

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    image = models.ImageField( default='profile_pics/default.jpg',  # Relative to MEDIA_ROOT
        upload_to='profile_pics',
        blank=True,
        null=True
    )
    # user = get_object_or_404(User, username='username')
    # Redirect to the user's profile page
    #  return redirect('profile', user.username)
    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height >300 or img.width >300:
            output_size =(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


def user_profile(request, username):
    # Get the user by username or return a 404 page if not found
    user = get_object_or_404(User, username='username')
    # Get the user's profile
    user_profile = get_object_or_404(profile, user=user)
    return render (request, 'user_profile.html', {'user_profile': user_profile})

    

    


    