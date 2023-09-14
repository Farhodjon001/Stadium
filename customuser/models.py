from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    CHOICES = (
        (3, 'admin'),
        (1, 'user'),
        (2, "manager")
    )
    roles = models.PositiveSmallIntegerField(default=1, choices=CHOICES)