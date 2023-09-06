from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# user are predefined in django authenciation system

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()  # content can be of any length so we use textfield
    
    date_posted = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def _str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})
    
    # user who crted the field

    # user module and post module have  relationship
    # because since user are going to author post
    # one to many realtionship becuse one user may
    # have many post but a post have only the one postiog
    # user

    # to implemt the one to many relationship we use
    # foreign key .





# user are predefined in django authenciation system

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"
