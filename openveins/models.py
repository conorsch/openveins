from django.db import models
from django.utils import timezone


class Quote(models.Model):

    class Meta:
        ordering = ['-post_date']

    author = models.CharField(max_length=100)
    source = models.CharField(max_length=100, blank=True, null=True)
    year = models.CharField(max_length=10, blank=True, null=True)
    editorial = models.TextField(blank=True)
    text = models.TextField(blank=True)
    raw_text = models.TextField(blank=True)
    post_date = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        if self.author:
            return "Author: {}, {}".format(self.author, self.text)
        return self.__class__.__name__
