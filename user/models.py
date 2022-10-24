from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    birthdate = models.DateField()
    bio = models.CharField(
        max_length=500,
        blank=True,
        null=True,
    )
    is_critic = models.BooleanField(
        default=False,
    )
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ["birthdate", "email", "first_name", "last_name"]
