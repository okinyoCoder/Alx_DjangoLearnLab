from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    class meta:
        ordering = 'title'

    def __str__(self):
        return self.title