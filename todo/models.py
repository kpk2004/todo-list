from django.db import models

# Create your models here.
class todolist(models.Model):
    todo=models.CharField(max_length=5000)
