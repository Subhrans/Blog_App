from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=128)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/post/', blank=True, null=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    profile_Image = models.ImageField(upload_to='images/')
    bio = models.TextField(null=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.user)
