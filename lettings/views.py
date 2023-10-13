# Django views module for the 'lettings' app.
# This module contains view functions for displaying a list of lettings
# and a specific letting.
# It uses data from the 'Letting' model and renders HTMLtemplates
# for the corresponding views.


from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from lettings.models import Letting


# Aenean leo magna, vestibulum et tincidunt fermentum,
# consectetur quis velit. Sed non placerat massa.
# Integer est nunc, pulvinar a tempor et, bibendum id arcu.
# Vestibulum ante ipsum primis in faucibus orci luctus et
# ultrices posuere cubilia curae; Cras eget scelerisque
def index(request: HttpRequest) -> HttpResponse:
    """View function for displaying a list of lettings.

    This view retrieves a list of lettings from the database and renders them
    in the 'lettings/index.html' template.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: A rendered HTML response displaying the list of lettings.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non.
# In accumsan porta nisl id eleifend. Praesent dignissim,
# odio eu consequat pretium, purus urna vulputate arcu,
# vitae efficitur lacus justo nec purus.
# Aenean finibus faucibus lectus at porta. Maecenas auctor,
# est ut luctus congue, dui enim mattis enim,
# ac condimentum velit libero in magna. Suspendisse potenti.
# In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum.
# Ut quis urna pellentesque justo mattis ullamcorper ac non tellus.
# In tristique mauris eu velit fermentum, tempus pharetra est luctus.
# Vivamus consequat aliquam libero, eget bibendum lorem.
# Sed non dolor risus.
# Mauris condimentum auctor elementum. Donec quis nisi ligula.
# Integer vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.
def letting(request: HttpRequest, letting_id: int) -> HttpResponse:
    """View function for displaying a specific letting.

    This view retrieves a specific letting from the database using the
    provided 'letting_id' and renders it in the
    'lettings/letting.html' template.

    Args:
        request (HttpRequest): The incoming HTTP request.
        letting_id (int): The unique identifier of the letting
        to be displayed.

    Returns:
        HttpResponse: A rendered HTML response displaying
        the specific letting.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
