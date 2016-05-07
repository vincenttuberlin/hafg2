from django.db import models
from datetime import date
# Create your models here.
class TodoItem(models.Model):
        description = models.CharField(max_length=5000)
        deadline = models.DateField(default=date.today)
        progress = models.SmallIntegerField(default=0)
