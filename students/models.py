from django.db import models
from django.contrib.auth.models import AbstractUser

class Student(AbstractUser):
    phone = models.CharField(max_length=15)
    address = models.CharField()
    profileImage = models.ImageField(upload_to='students/covers/',null=True,blank=True)

    def __str__(self):
        return self.username
    
    @property
    def image_url(self):
        return f'/media/{self.profileImage}'
