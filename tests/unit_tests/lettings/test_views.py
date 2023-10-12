"""Module of testing views .py of lettings app """

from django.test import Client
from django.urls import reverse

import pytest
from pytest_django.asserts import assertTemplateUsed

from lettings.models import Letting, Address

client = Client()


class TestView:
    def _create_addres(self, number, street):
        address = Address.objects.create(
            number=number,
            street=street,
            city="bayonne",
            state="FR",
            zip_code="64100",
            country_iso_code="aze",
        )
        return address

    def _create_letting(self, address, title):
        return Letting.objects.create(title=title, address=address)

    @pytest.mark.django_db
    def test_index_views(self):
        """Testing if index() is rendered properly by checking
        200 status code.
        We Testing if "lettings/index.html" template is rendered,
        we create an address and letting to make sure that context
        is rendered correctly.
        """
        address = self._create_addres(number=41, street="street_test")
        letting = self._create_letting(address=address, title="a title leting")
        response = client.get(reverse("lettings_index"))
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/index.html")
        lettings_list = Letting.objects.all()
        context = response.context
        assert letting in context["lettings_list"]
        assert len(lettings_list) == len(context["lettings_list"])

    @pytest.mark.django_db
    def test_letting_views(self):
        """Testing if letting is rendered properly by checking
        200 status code.
        We Testing if "lettings/letting.html" template is rendered,
        we create an address and letting to make sure that context
        is returned  correctly a letting created.
        """
        address = self._create_addres(number=41, street="street_test")
        letting = self._create_letting(address=address, title="a title leting")
        response = client.get(reverse("letting", args=[1]))
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/letting.html")
        context = response.context
        assert context["title"] == letting.title
        assert context["address"] == letting.address
