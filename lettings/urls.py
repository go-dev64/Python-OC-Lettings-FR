# Module of urls of lettings app. It define the url of each views.

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="lettings_index"),
    path("<int:letting_id>/", views.letting, name="letting"),
]
