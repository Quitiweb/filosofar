from django.db import models

TITLE = 100
TEXT = 1500

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = TITLE)
    body = models.TextField(max_length = TEXT)
    date = models.DateTimeField()

    def __str__(self):
        return self.date + " - " + self.title