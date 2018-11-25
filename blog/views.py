from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . import models

# Create your views here.
#def index(request):
#    return render(request, 'blog/index.html')

def single(request):
    return render(request, 'blog/single.html')

def index(request):
    post_list = models.Post.objects.all()
    template = loader.get_template('blog/index.html')

    context = {
        'post_list': post_list,
    }

    return HttpResponse(template.render(context, request))