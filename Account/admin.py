from django.contrib import admin
from .models import NewsDetails, Comment, Games



# Register your models here.
class AdminNewsDetails(admin.ModelAdmin):
    pass

admin.site.register(NewsDetails,AdminNewsDetails)


class AdminComment(admin.ModelAdmin):
    pass
admin.site.register(Comment,AdminComment)




class AdminGames(admin.ModelAdmin):
    pass
admin.site.register(Games,AdminGames)

'''
from django.db import models

from taggit.managers import TaggableManager


class Food(models.Model):
    # ... fields here

    tags = TaggableManager()
Then you can use the API like so:

>>> apple = Food.objects.create(name="apple")
>>> apple.tags.add("red", "green", "delicious")
>>> apple.tags.all()
[<Tag: red>, <Tag: green>, <Tag: delicious>]
>>> apple.tags.remove("green")
>>> apple.tags.all()
[<Tag: red>, <Tag: delicious>]
>>> Food.objects.filter(tags__name__in=["red"])
[<Food: apple>, <Food: cherry>]2++
'''
