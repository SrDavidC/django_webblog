from django.db import models;

class Message(models.Model):
    personName = models.CharField(max_length=50)
    personEmail = models.CharField(max_length=50)
    message = models.TextField()
    