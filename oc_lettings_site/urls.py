# Module of urls of oc_lettings_site app. It define the url of each views.


from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path("admin/", admin.site.urls),
]


handler404 = "oc_lettings_site.views.handler404"
handler500 = "oc_lettings_site.views.error500"
