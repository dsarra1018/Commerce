from django.contrib.auth.models import AbstractUser
from django.db import models

# User model
class User(AbstractUser):
    pass


# Category model
class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.category}"