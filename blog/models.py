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
class SecondarySchool(models.Model):
    name = models.CharField(max_length=200)
    join_date = models.DateField()
    end_date = models.DateField()
    completed = models.BooleanField(default=False)

class HigherSecondarySchool(models.Model):
    name = models.CharField(max_length=200)
    join_date = models.DateField()
    end_date = models.DateField()
    completed = models.BooleanField(default=False)

class College(models.Model):
    name = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    join_date = models.DateField()
    end_date = models.DateField()
    completed = models.BooleanField(default=False)

class UserProfile(models.Model):
    profile_Image = models.ImageField(upload_to='images/', null=True)
    bio = models.TextField(null=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    cover_Image = models.ImageField(upload_to='images/cover_img/', null=True, blank=True)
    secondary_school = models.ForeignKey(SecondarySchool, null=True, blank=True, on_delete=models.DO_NOTHING)
    higher_secondary_school = models.ForeignKey(HigherSecondarySchool, null=True, blank=True, on_delete=models.DO_NOTHING)


    def __str__(self):
        return "{}".format(self.user)
