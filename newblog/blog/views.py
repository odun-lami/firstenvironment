from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def homepage(request):


    posts = Post.objects.all()
    header = 'odunlami'

    return render (request, 'index.html', {'titles':posts, 'header':header})