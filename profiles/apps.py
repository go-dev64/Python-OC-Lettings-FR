# Django application configuration for the 'profiles' app.
# This module defines the configuration for the 'profiles' app, including its name.

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """Configuration class for the 'profiles' app.

    This class defines the configuration for the 'profiles' app, including its name.

    Attributes:
        name (str): The name of the Django app, which is 'profiles'.
    """

    name = "profiles"
