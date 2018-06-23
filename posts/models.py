from django.db import models
from datetime import datetime, timedelta


# Create your models here.
class Post(models.Model):
    title = models.CharField("Title", max_length=100)
    desc = models.CharField("Description", max_length=1000)
    timestamp = models.DateTimeField("Created Timestamp", auto_now_add=True)

    def __str__(self):
        return self.title

    def print_title_desc(self):
        return self.title + "|" + self.desc

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Post"