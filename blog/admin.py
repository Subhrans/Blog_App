from django.contrib import admin
from .models import Post,UserProfile,Category,HigherSecondarySchool,SecondarySchool,College
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','user','creation_date']
    list_display_links = ['title','id']
    list_filter = ['title','creation_date','user','description','id','category']
    list_per_page = 10
    search_fields = ['title']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','profile_Image']
    list_display_links = ['id','user']
    list_filter = ['user', 'bio', 'id']
    list_per_page = 10
    search_fields = ['user']


@admin.register(Category)
class ChategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_per_page = 10
    search_fields = ['name','id']

# @admin.register(Like)
# class LikeAdmin(admin.ModelAdmin):
#     list_display = ['id','like_post','like_by']
#     list_per_page = 10
#     search_fields = ['like_post','like_by']