from django.db import models
from tinymce import HTMLField

class ProductType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Scenario(models.Model):
    name = models.CharField(max_length=200)
    description = HTMLField()
    procedures = HTMLField(blank=True)
    product = models.ForeignKey('ProductType', on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Notification(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=200)
    answer = HTMLField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Tool(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.name
