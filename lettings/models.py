# Models module of lettins app.
# it define each models of app.
# Each models represent a databse table.

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """model representing an adres in the application.

    Attributes:
        number (PositiveIntegerField): Numero of street
        street (CharField): Street name.
        city (CharField): City name.
        state (CharField): Code of state : 2 characteres max (pex. "NY" for New York).
        zip_code (PositiveIntegerField): Postal code.
        country_iso_code (CharField): ISO code of country 2 characteres max( ex. "USA").

    Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    Methods:
        __str__(): Returns a string representation of the address (number and street).

    Returns:
        str:  a string representation of the address.
    """

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self) -> str:
        """Returns a string representation of the Address object.

        The string representation is formatted as 'number street', for example, '123 Main St'.

        Returns:
            str: A string representing the Address('number street').
        """
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """Model representing a letting (rental) in the application.

    Attributes:
        title (CharField): The title or name of the letting.
        address (OneToOneField): The instance of Address associated with the letting.

    Methods:
        __str__(): Returns a string representation of the letting (its title).

    Returns:
        str: A string representing the letting.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """Returns a string representation of the Letting object.
        Returns:
            str: A string representing the Letting title.
        """
        return self.title
