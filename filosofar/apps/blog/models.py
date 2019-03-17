from django.db import models
from tinymce.models import HTMLField

TITLE = 100
TEXT = 15000


class Post(models.Model):
    title = models.CharField(max_length=TITLE)
    subtitle = models.CharField(max_length=TITLE, default='')
    body = HTMLField(max_length=TEXT, default='', blank=True)
    date = models.DateTimeField()
    main_pic = models.ImageField(upload_to='img/post/')

    def __str__(self):
        return self.date.strftime('%Y-%m-%d') + " - " + self.title


class Imagen(models.Model):
    imgFile = models.ImageField(upload_to='img/')
