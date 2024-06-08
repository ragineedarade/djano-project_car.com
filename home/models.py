from django.db import models

# Create your models here.
# makemigrations - create changes and store in a file
# migrate  apply the pendling create by makemigrate


class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=120)
    message = models.CharField(max_length=1000)
    date = models.DateField()


def ___str__(self):
    return self.name
