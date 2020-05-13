import os
from django.db import models

class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file.name

    def get_filename(self):
        return os.path.basename(self.file.name)