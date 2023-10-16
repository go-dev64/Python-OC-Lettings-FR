"""Module of testing views .py of lettings app """

from django.test import Client, RequestFactory
from django.urls import reverse

import pytest
from pytest_django.asserts import assertTemplateUsed


from lettings.models import Letting, Address
from lettings.views import index, letting

client = Client()


class TestView:
    def _create_addres(self, number, street):
        """This class contains unit tests for the views
        in the 'lettings' app.

        These tests check if the views are rendering the
        correct templates and
        returning the expected HTTP status codes.
        The returned contex will also be chexked.
        """
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
        We Testing if "lettings/index.html" template is rendered.
        """
        response = client.get(reverse("lettings_index"))
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/index.html")

    @pytest.mark.django_db
    def test_index_views_with_exception(self, mocker):
        """Testing if error page is rendered properly by checking
        400 status code when there are an exception raises..
        """
        mock_test = mocker.patch.object(Letting.objects, "all")
        mock_test.side_effect = Exception()
        result = index("test")
        assert result.status_code == 400

    @pytest.mark.django_db
    def test_letting_views(self):
        """Testing if letting is rendered properly by checking
        200 status code.
        We Testing if "lettings/letting.html" template is rendered,
        we create an address and letting to make sure that context
        is returned  correctly a letting created.
        """
        address = self._create_addres(number=41, street="street_test")
        self._create_letting(address=address, title="a title leting")
        response = client.get(reverse("letting", args=[1]))
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/letting.html")

    @pytest.mark.django_db
    def test_letting_views_with_bad_index(self):
        """Testing if error page with bad index is rendered properly
        by checking 404 status code.
        We Testing if "error.html" template is rendered,
        """
        response = client.get(reverse("letting", args=[2]))
        assert response.status_code == 404
        assertTemplateUsed(response, "error_page.html")

    @pytest.mark.django_db
    def test_letting_views_with_exception(self, mocker):
        """Testing if eror page with  is rendered properly by checking
        400 status code when there are an exception raises.
        """
        mock_test = mocker.patch.object(Letting.objects, "get")
        mock_test.side_effect = Exception()
        result = letting("test", "test")
        assert result.status_code == 400
