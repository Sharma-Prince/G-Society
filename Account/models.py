from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from taggit.managers import TaggableManager
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, to_field='username')
    phone = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username



class NewsDetails(models.Model):
    ImgUrl = models.URLField(max_length = 1000)
    NewsTitle = models.CharField(max_length=255, null=True, blank=True)
    Platform = models.CharField(max_length=80)
    like = models.BooleanField(default=False)
    NewsBody = models.TextField()
    active = models.BooleanField(default=False)
    detailBody = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Games(models.Model):
    ImgUrl = models.URLField(max_length = 1000)
    GameTitle = models.CharField(max_length=255, null=True, blank=True)
    Platform = models.CharField(max_length=80)
    Like = models.BooleanField(default=False)
    description = models.TextField()
    Active = models.BooleanField(default=True)
    DetailBody = models.TextField()
    Tags = TaggableManager()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Comment(models.Model):
    content_type  = models.ForeignKey(ContentType,  on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE,blank=True, related_name='replies')
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
