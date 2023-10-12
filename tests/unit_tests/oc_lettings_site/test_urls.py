"""
This module contains test functions related to URL routing in
'oc_lettings_site' app.

The functions included here are designed to test the URL routing
configuration and mapping of views to specific URL patterns
in the 'oc_lettings_site' app.
"""


from django.urls import reverse, resolve


def test_profiles_index_url():
    """Testing if the 'profiles_index' route maps to our index view."""

    url = reverse("profiles_index")
    assert resolve(url).view_name == "profiles_index"


def test_profile_url():
    """Testing if the 'profile' route maps to our letting view."""

    url = reverse("profile", args=[1])
    assert resolve(url).view_name == "profile"
