"""Module of testing views .py of oc_lettings_site app """

from django.test import Client
from django.urls import reverse

from pytest_django.asserts import assertTemplateUsed

client = Client()


def test_index_views():
    """
    Testing if index() is rendered properly by checking
    200 status code.
    """
    response = client.get(reverse("index"))
    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")


def test_404_error_view():
    """Testing if, with a not found request, 404.html is rendered."""
    response = client.get("fvqdrgd")
    assert response.status_code == 404
    assertTemplateUsed(response, "404.html")
