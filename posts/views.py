from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
from itertools import chain
from operator import attrgetter

# Create your views here.
def index(request):
    # return HttpResponse('Hello FROM POSTS')
    print("index has fired")
    posts = Posts.objects.all()

    result_list = sorted(
        chain(posts),
        key=attrgetter('created_at'),
        reverse = True
    )[:10]

    context = {
        'title' : 'Latest Posts',
        'posts': result_list
    }
    return render(request, 'posts/index.html', context)

def details(request,id):
    post = Posts.objects.get(id=id)

    context = {
        'post': post
    }
    return render(request, 'posts/details.html', context)
