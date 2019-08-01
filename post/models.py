from django.db import models
from django.utils import timezone
# Create your models here.



class Post(models.Model):
    """docstring for Post."""
    auther = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=100)
    text = models.TextField(blank=True)
    created_date = models.DateTimeField(blank=True, default=timezone.now)
    published_date = models.DateTimeField(null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()





    def __str__(self):
        return self.title
