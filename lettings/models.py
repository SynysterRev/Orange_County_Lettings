from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


class Address(models.Model):
    """
        Model representing an address.

        This model stores address details such as street number, street name,
        city, state, postal code, and country ISO code.

        Attributes:
            number (int): The house/building number in the address.
            It is a positive integer with a maximum value of 9999.
            street (str): The street name of the address.
            city (str): The city of the address.
            state (str): The state of the address. It must be a 2-character string.
            zip_code (int): The postal code of the address. It is a positive integer
            with a maximum value of 99999.
            country_iso_code (str): The ISO code of the country. It is a 3-character string.
        """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3,
                                        validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
        Model representing a letting (property rental).

        This model stores details about a letting, including the title of the property
        and the associated address.

        Attributes:
            title (str): The title or name of the letting (e.g., "Cozy Apartment").
            address (Address): The address associated with this letting,
            which is linked to the `Address` model.
        """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
