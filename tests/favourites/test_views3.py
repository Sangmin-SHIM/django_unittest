# tests/favourites/tests_views2.py
from django.test import Client
from django.urls import reverse, resolve

import pytest
from users.models import User

client = Client()


@pytest.mark.django_db
def test_favourite_product_list_view():

    # Préparation
    user = User.objects.create_user(username='testuser', password='TestPassword')

    # Action
    client.force_login(user)
    client.login(username='testuser', password='TestPassword')
    response = client.get(reverse("favourite-products"))

    # Assertion
    assert response.status_code == 200