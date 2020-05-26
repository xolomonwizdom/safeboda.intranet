from django.db import models
from tinymce import HTMLField

class Category(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Activity(models.Model):
    title = models.CharField(max_length=120)
    description = HTMLField()
    steps = HTMLField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Activities'


class TicketType(models.Model):
    title = models.CharField(max_length=120)
    content = HTMLField()

    def __str__(self):
        return self.title

    class Meta:
        pass