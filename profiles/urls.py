# Module of urls of profiles app. It define the url of each views.
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="profiles_index"),
    path("<str:username>/", views.profile, name="profile"),
]
