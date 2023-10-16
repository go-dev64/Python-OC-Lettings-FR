from lettings.models import Address, Letting


import pytest


class TestModels:
    """This is test class of models ' s lettings."""

    credentials = {
        "number": 41,
        "street": "rue",
        "city": "bayonne",
        "state": "FR",
        "zip_code": "64100",
        "country_iso_code": "aze",
    }

    @pytest.mark.django_db
    def test_address_str(self):
        """
        Testing whether Address's __str__ method is implemented properly.
        """

        address = Address.objects.create(
            number=self.credentials["number"],
            street=self.credentials["street"],
            city=self.credentials["city"],
            state=self.credentials["state"],
            zip_code=self.credentials["zip_code"],
            country_iso_code=self.credentials["country_iso_code"],
        )

        assert str(address) == f"{self.credentials['number']} {self.credentials['street']}"

    @pytest.mark.django_db
    def test_lettings_str(self):
        """
        Testing whether Lettings's __str__ method is implemented properly.
        """

        address = Address.objects.create(
            number=self.credentials["number"],
            street=self.credentials["street"],
            city=self.credentials["city"],
            state=self.credentials["state"],
            zip_code=self.credentials["zip_code"],
            country_iso_code=self.credentials["country_iso_code"],
        )
        letting = Letting.objects.create(title="a title leting", address=address)
        assert str(letting) == "a title leting"
