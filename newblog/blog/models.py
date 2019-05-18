from django.db import models
from django.conf import settings


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    title=models.CharField(max_length=70)
    body=models.TextField()
    published=models.DateTimeField()

    def __str__(self):

        return self.title