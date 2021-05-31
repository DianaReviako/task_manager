from datetime import date
from django.db import models


class Task(models.Model):
    deadline_date = models.DateField(null=True)
    create_date = models.DateField(default=date.today)
    text = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.text
