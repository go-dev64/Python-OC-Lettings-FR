import pytest
from django.test import Client


def client():
    client = Client()
    return client
