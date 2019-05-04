from django.db import models

# Create your models here.
class Post(models.Model):

    title=models.CharField(max_length=70)
    body=models.TextField()
    published=models.DateTimeField()

    def __str__(self):

      return '{} published on {}'.format(self.title + self.published)