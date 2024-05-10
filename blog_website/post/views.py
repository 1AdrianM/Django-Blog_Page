from django.shortcuts import render
from .models import Post
# Create your views here.

def posts_list(request):
    post = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': post})