from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='authentication_profile')
    age = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    religion = models.CharField(max_length=100, blank=True, null=True)
    region_of_residence = models.CharField(max_length=100, blank=True, null=True)
    tribe = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username
