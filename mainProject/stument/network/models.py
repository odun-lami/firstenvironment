from django.db import models

# Create your models here.
class Profile(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    title=models.CharField(max_length=70)
    body=models.TextField()
    published=models.DateTimeField()