# Models module of profiles app.
# it define each models of app.
# Each models represent a databse table.

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    """Model representing a user's profile in the application.

    This model is used to store additional information about a user, such as their
    favorite city. It is linked to the built-in 'User' model through a one-to-one
    relationship.

    Attributes:
        user (OneToOneField): The user associated with the profile.
        favorite_city (CharField): The user's favorite city (optional).

    Methods:
        __str__(): Returns a string representation of the user's profile (the username).

    Returns:
        str: A string representing the user's profile.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self) -> str:
        """The function return a strinf occurinf username of user's.

        Returns:
            str: str of username user's.
        """
        return self.user.username
