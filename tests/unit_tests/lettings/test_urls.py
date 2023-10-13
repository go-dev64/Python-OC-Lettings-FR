"""
This module contains test functions related to URL routing
in 'lettings' app.

The functions included here are designed to test
the URL routing configuration and mapping of views to
specific URL patterns in the 'lettings' app.
"""


from django.urls import reverse, resolve


def test_lettings_index_url():
    """Testing if the 'lettings_index' route maps to our index view."""

    url = reverse("lettings_index")
    assert resolve(url).view_name == "lettings_index"


def test_letting_url():
    """Testing if the 'letting' route maps to our letting view."""

    url = reverse("letting", args=[1])
    assert resolve(url).view_name == "letting"
