from django.db import models

# Create your models here.

class Image(models.Model):
    url = models.TextField()

    def __str__(self):
        return self.url

class Text(models.Model):
    text = models.TextField()

    def __str__(self):
        return "{id: %s, text: %s}" % (self.id, self.text)
