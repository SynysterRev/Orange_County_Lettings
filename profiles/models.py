from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
        Model representing a user profile.

        This model is linked to a User via a OneToOne relationship and contains information
        about the user's favorite city.

        Attributes:
            user (User): The user to whom this profile belongs.
            favorite_city (str): The user's favorite city. Can be empty.
        """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
