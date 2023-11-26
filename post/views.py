from django.shortcuts import render
from .models import Post, Media
 
def main(request):
    posts = Post.objects.all()
    medias = Media.objects.all()
    return render(request=request,template_name='main.html',context={'posts':posts, 'medias':medias})
