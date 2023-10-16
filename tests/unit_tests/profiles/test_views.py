"""Module of testing views.py of Profile app """

from django.test import Client
from django.urls import reverse, resolve

import pytest
from pytest_django.asserts import assertTemplateUsed

from profiles.models import Profile, User
from profiles.views import index, profile

client = Client()


class TestView:
    """This class contains unit tests for the views
    in the 'profiles' app.

    These tests check if the views are rendering the
    correct templates and
    returning the expected HTTP status codes.
    The returned contex will also be chexked.
    """

    def _create_profile(self, username):
        user = User.objects.create(username=username, password="toto")
        profile = Profile.objects.create(user=user)
        return profile

    @pytest.mark.django_db
    def test_index_views(self):
        """Testing if index() is rendered properly by checking
        200 status code.
        We Testing if "profiles/index.html" template is rendered.
        """
        response = client.get(reverse("profiles_index"))
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/index.html")

    @pytest.mark.django_db
    def test_index_views_with_exception(self, mocker):
        """Testing if error page is rendered properly by checking
        400 status code when there are an exception raises.
        """
        mock_test = mocker.patch.object(Profile.objects, "all")
        mock_test.side_effect = Exception()
        result = index("test")
        assert result.status_code == 400

    @pytest.mark.django_db
    def test_profile_views(self, mocker):
        """Testing if profile is rendered properly by checking
        200 status code.
        We Testing if "profiles/profile.html" template is rendered,
        we create  profiles to make sure that context is returned
        correctly a profiles created.
        """
        mock_test = mocker.patch.object(Profile.objects, "get")
        mock_test.side_effect = ["test_profile", "toto"]
        response = client.get(reverse("profile", args=["test_profile"]))
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/profile.html")

    @pytest.mark.django_db
    def test_profile_views_with_bad_index(self):
        """Testing if error page with bad index is rendered properly
        by checking 404 status code.
        We Testing if "error.html" template is rendered,
        """
        response = client.get(reverse("profile", args=[2]))
        assert response.status_code == 404
        assertTemplateUsed(response, "error_page.html")

    @pytest.mark.django_db
    def test_profile_views_with_exception(self, mocker):
        """Testing if eror page with  is rendered properly by checking
        400 status code when there are an exception raises.
        """
        mock_test = mocker.patch.object(Profile.objects, "get")
        mock_test.side_effect = Exception()
        result = profile("test", "test")
        assert result.status_code == 400
