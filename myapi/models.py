
from django.db import models

# Create your models here.
class Title(models.Model):
    name = models.CharField(с=60)
    description = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class TextField(models.Model):
    description = ("Text")

    def get_internal_type(self):
        return "TextField"