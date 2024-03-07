# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Crush(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    online = models.BooleanField(default=False)
    # Add more fields as needed
