"""Module of testing views.py of Profile app """

from django.test import Client
from django.urls import reverse

import pytest
from pytest_django.asserts import assertTemplateUsed

from profiles.models import Profile, User

client = Client()


class TestView:
    def _create_profile(self, username):
        user = User.objects.create(username=username, password="toto")
        profile = Profile.objects.create(user=user)
        return profile

    @pytest.mark.django_db
    def test_index_views(self):
        """Testing if index() is rendered properly by checking
        200 status code.
        We Testing if "profiles/index.html" template is rendered,
        we create Profiles to make sure that context is rendered
        correctly.
        """
        profile_1 = self._create_profile(username="test_profile")
        profile_2 = self._create_profile(username="test_profile2")
        response = client.get(reverse("profiles_index"))
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/index.html")
        profiles_list = Profile.objects.all()
        context = response.context
        assert profile_1 in context["profiles_list"]
        assert profile_2 in context["profiles_list"]
        assert len(profiles_list) == len(context["profiles_list"])

    @pytest.mark.django_db
    def test_letting_views(self):
        """Testing if profile is rendered properly by checking
        200 status code.
        We Testing if "profiles/profile.html" template is rendered,
        we create  profiles to make sure that context is returned
        correctly a profiles created.
        """
        profile_1 = self._create_profile(username="test_profile")
        profile_2 = self._create_profile(username="test_profile2")
        response = client.get(reverse("profile", args=["test_profile"]))
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/profile.html")
        context = response.context
        assert context["profile"] == profile_1
        response_2 = client.get(reverse("profile", args=["test_profile2"]))
        context_2 = response_2.context
        assert context_2["profile"] == profile_2
