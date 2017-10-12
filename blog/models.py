from django.db import models


# Create your models here.
class Topic(models.Model):
    title = models.TextField(max_length=100)
    content = models.TextField(max_length=100000)
    publish_time = models.DateTimeField(auto_now_add=True)
    tag = models.TextField(max_length=100)


class Comment(models.Model):
    tid = models.ForeignKey(to=Topic)
    username = models.TextField(max_length=100)
    email = models.TextField(max_length=100)
    content = models.TextField(max_length=1000)
    publish_time = models.DateTimeField(auto_now_add=True)


class Variable(models.Model):
    keyName = models.TextField(max_length=30)
    keyValue = models.TextField(max_length=50)
