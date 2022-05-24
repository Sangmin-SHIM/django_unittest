# tests/favourites/tests_views2.py
from django.test import Client
from django.urls import reverse, resolve

import pytest
from users.models import User

client = Client()


@pytest.mark.django_db
def test_favourite_product_list_view():
    
    credentials = {
        'first_name' : 'Test',
        'last_name' : 'User',
        'username' : 'testuser',
        'email' : 'testuser@testing.com',
        'password1' : 'TestPassword',
        'password2' : 'TestPassword'
    }
    # Préparation
    user = User.objects.create_user(username=credentials['username'], password=credentials['password1'])

    client.force_login(user)
    client.login(username=credentials['username'], password=credentials['password1'])
    response = client.get(reverse("favourite-products"))

    assert response.status_code == 200