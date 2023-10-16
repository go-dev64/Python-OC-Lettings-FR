# Django views module for the 'profiles' app.
# This module contains view functions for displaying a list of lettings
# and a specific profile.
# It uses data from the 'profile' model and renders HTML templates
# for the corresponding views.


import logging
from django.http import Http404
from django.shortcuts import render
from profiles.models import Profile


# Sed placerat quam in pulvinar commodo.
# Nullam laoreet consectetur ex, sed consequat libero pulvinar eget.
# Fusc faucibus, urna quis auctor pharetra, massa dolor cursus neque,
# quis dictum lacus d
def index(request):
    """View function for displaying a list of profiles.

    This view retrieves a list of lettings from the database and
    renders them in the 'profiles/index.html' template.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: A rendered HTML response displaying
        the list of profiles.
    """
    try:
        profiles_list = Profile.objects.all()
    except Exception as e:
        logging.exception(e)
        return render(request, "error_page.html", context={"error": e}, status=400)
    else:
        context = {"profiles_list": profiles_list}
        return render(request, "profiles/index.html", context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan
# eget lac laoreet neque quis,pellentesque dui.
# Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla,
# eros leo tristique lacus,it. Nam aliquam dignissim congue.
# Pellentesque habitant morbi tristique senectus et netus et males.
def profile(request, username):
    """View function for displaying a specific profile.

    This view retrieves a specific letting from the database using
    the provided 'profile_id' and renders
    it in the 'profiles/profile.html' template.

    Args:
        request (HttpRequest): The incoming HTTP request.
        letting_id (int): The unique identifier of the profile
        to be displayed.

    Returns:
        HttpResponse: A rendered HTML response displaying
        the specific profile.
    """
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        raise Http404
    except Exception as e:
        logging.exception(e)
        return render(request, "error_page.html", context={"error": e}, status=400)

    else:
        context = {"profile": profile}
        return render(request, "profiles/profile.html", context)
