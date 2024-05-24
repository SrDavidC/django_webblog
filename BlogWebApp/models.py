from django.db import models;

from djangoProject import settings


class Message(models.Model):
    personName = models.CharField(max_length=50)
    personEmail = models.CharField(max_length=50)
    message = models.TextField()

    def is_valid(self):
        pass
    # TO DO: check if it is necessary

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    thumbnail_url = models.URLField()
    preview_text = models.TextField()
    text = models.TextField(default="")
    readingTimeInMinutes = models.IntegerField()
    categories = models.TextField() # Could be text field separated by comma: academic, biological, vacations or with foreign key.
    publicationDate = models.DateField
    author = models.CharField(max_length=50, default=settings.DEFAULT_BLOG_AUTHOR)
    likesCount = models.IntegerField(default=0)

    def __str__(self):
        return self.title

