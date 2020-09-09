from django.db import models

# Create your models here.
class Post(models.Model):

    author = models.CharField(max_length=10)
    subject = models.CharField(max_length=30)
    body = models.TextField()
    image = models.ImageField( upload_to='image', blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.author} :{self.body}'
    