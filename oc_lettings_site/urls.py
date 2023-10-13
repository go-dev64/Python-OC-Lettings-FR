# Module of urls of oc_lettings_site app. It define the url of each views.


from django.contrib import admin
from django.urls import path, include

from . import views


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path("sentry-debug/", trigger_error),
    path("admin/", admin.site.urls),
]


handler404 = "oc_lettings_site.views.handler404"
handler500 = "oc_lettings_site.views.error500"
