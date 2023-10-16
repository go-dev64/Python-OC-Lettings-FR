from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from sentry_sdk import capture_message


# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Quisque molestie quam lobortis leo consectetur ullamcorper
# non id est.
# Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem.
# Maecenas pharetra purus ipsum, eget consequat ipsum lobortis quis.
# Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus.
# Nullam elementum urna nisi, pellentesque iaculis enim cursus in.
# Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request: HttpRequest) -> HttpResponse:
    """the function return the home page of wesite.

    Args:
        request (HttpRequest): The object representing
        the incoming HTTP request.

    Returns:
        HttpResponse: return index.html template.
    """

    return render(request, "index.html")


def handler404(request: HttpRequest, exception: Exception) -> HttpResponse:
    """The function return a customized 404 error page.

    Args:
        request (HttpRequest): The object representing
        the incoming HTTP request
        exception (Exception): The exception raised when
        a 404 error occurs.

    Returns:
        HttpResponse:  return 404.html template.
    """
    capture_message("Page not found!", level="info")
    return render(request, "error_page.html", context={"error": "404 - Not Fonud"}, status=404)


def error500(request: HttpRequest) -> HttpResponse:
    """The function is used to return a customized
    500 Server Internal error page.

    Args:
        request (HttpRequest): The object representing
        the incoming HTTP request

    Returns:
        HttpResponse:  return 500.html template.
    """
    capture_message("Server internal", level="error")
    return render(
        request, "error_page.html", context={"error": "500 - Sever Internat Error"}, status=500
    )
