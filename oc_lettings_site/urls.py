from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler403, handler500

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path("admin/", admin.site.urls),
]


handler403 = "oc_lettings_site.views.handler404"
handler500 = "oc_lettings_site.views.handler500"
