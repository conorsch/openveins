from django.db import models
from datetime import datetime


class Quote(models.Model):

    author = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    year = models.CharField(max_length=10, blank=True, null=True)
    editorial = models.TextField(blank=True)
    text = models.TextField(blank=True)
    raw_text = models.TextField(blank=True)
    post_date = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        if self.author:
            return "Author: {}, {}".format(self.author, self.text)
        return self.__class__.__name__
