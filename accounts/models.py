from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone_number=models.CharField(max_length=20)
    birthday=models.DateField(null=True, blank=True)
    location=models.CharField(max_length=20)

    # add additional fields in here

    def __str__(self):
        return self.username
