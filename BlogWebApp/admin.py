from django.contrib import admin

# Register your models here.
from .models import Message
from .models import BlogPost

admin.site.register(Message)

admin.site.register(BlogPost)
