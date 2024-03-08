from datetime import datetime

from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateTimeField(default=datetime.now())
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

