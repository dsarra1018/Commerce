from django.contrib.auth.models import AbstractUser
from django.db import models

# User model
class User(AbstractUser):
    pass


# Listing model
class Listing(models.Model):
    pass


# Bid model
class Bid(models.Model):
    pass


# Comment model
class Comment(models.Model):
    pass


# Category model
class Category(models.Model):
    pass