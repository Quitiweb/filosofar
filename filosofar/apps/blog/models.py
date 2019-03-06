from django.db import models

TITLE = 100
TEXT = 15000

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = TITLE)
    subtitle = models.CharField(max_length = TITLE, default='Post subtitle')
    body = models.TextField(max_length = TEXT)
    date = models.DateTimeField()
    mainPic = models.ImageField(upload_to='img/post/')

    def __str__(self):
        return self.date.strftime('%Y-%m-%d') + " - " + self.title

class Imagen(models.Model):
    imgFile = models.ImageField(upload_to='img/')
