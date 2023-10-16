"""This module test models of profile application.

"""


from django.contrib.auth.models import User
from profiles.models import Profile


import pytest


@pytest.mark.django_db
def test_profile_str():
    """
    Testing whether Profile's __str__ method is implemented properly.
    """
    user = User.objects.create(username="TestUser", password="toto")
    profile = Profile()
    profile.user = user
    assert str(profile) == "TestUser"
