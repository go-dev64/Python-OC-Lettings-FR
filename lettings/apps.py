# Django application configuration for the 'lettings' app.
# This module defines the configuration for the 'lettings' app, including its name.

from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """Configuration class for the 'lettings' app.

    This class defines the configuration for the 'lettings' app, including its name.

    Attributes:
        name (str): The name of the Django app, which is 'lettings'.
    """

    name = "lettings"
