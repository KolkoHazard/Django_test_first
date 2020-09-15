from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email=models.EmailField(max_length=264,unique=True)

    def __str__(self):
        return self.last_name
