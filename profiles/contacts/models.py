from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Contacts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, blank=False)
    phone_number = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return '%s' % self.name
