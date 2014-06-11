from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField()
    introduction = models.TextField()