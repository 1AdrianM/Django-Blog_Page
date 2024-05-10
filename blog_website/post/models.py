from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(unique=True)
    banner=models.ImageField(default='', blank=True, null=True)
    
    def __str__(self):
        
        return self.title