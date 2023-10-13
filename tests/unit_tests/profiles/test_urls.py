"""
This module contains test functions related to URL routing in
'oc_lettings_site' app.

The functions included here are designed to test the URL routing
configuration and mapping of views to specific URL patterns
in the 'oc_lettings_site' app.
"""


from django.urls import reverse, resolve
from oc_lettings_site import views


def test_index_url():
    """Testing if the 'index' route maps to our index view."""

    url = reverse("index")
    assert resolve(url).view_name == "index"
    assert resolve(url).func == views.index
