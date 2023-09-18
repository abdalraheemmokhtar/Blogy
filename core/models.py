from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    publication_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title