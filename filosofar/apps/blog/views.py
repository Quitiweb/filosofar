from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from . import models
from . import forms
from .tasks import simulate_send_emails

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

def member(request):
    if request.method == 'POST':
        form = forms.ImageForm(request.POST, request.FILES)
        if form.is_valid():
            newPic = models.Imagen(imgFile = request.FILES['imgFile'])
            newPic.save()
            
            return HttpResponseRedirect(reverse('member'))
    else:
        form = forms.ImageForm()

    images = models.Imagen.objects.all()

    return render(request, 'blog/member.html', {'images': images, 'form': form})

def send_emails(request):
    simulate_send_emails.delay(10)  # @UndefinedVariable
    return HttpResponse('Emails sent using Celery')