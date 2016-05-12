from django.db import models
from datetime import date
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
# Create your models here.
class TodoItem(models.Model):
        description = models.CharField(max_length=5000)
        deadline = models.DateField(default=date.today)
        progress = models.PositiveIntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100)])
