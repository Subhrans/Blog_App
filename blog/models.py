from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128,unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=128)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # description = models.TextField()
    description = RichTextField(blank=True,null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=128,default="coding")
    image = models.ImageField(upload_to='images/post/', blank=True, null=True)
    like = models.ManyToManyField(User,related_name="Post")

    def totalLike(self):
        return self.like.count()

    def __str__(self):
        return '{} of {}'.format(self.title, self.id)


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
    profile_Image = models.ImageField(default="images/default_profile/default-profile.jpg", upload_to='images/profile_pic/')
    bio = models.TextField(null=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    cover_Image = models.ImageField(upload_to='images/cover_img/', null=True, blank=True)
    secondary_school = models.ForeignKey(SecondarySchool, null=True, blank=True, on_delete=models.DO_NOTHING)
    higher_secondary_school = models.ForeignKey(HigherSecondarySchool, null=True, blank=True, on_delete=models.DO_NOTHING)


    def __str__(self):
        return "{}".format(self.user)
