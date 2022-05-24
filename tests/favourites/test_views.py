# tests/favourites/tests_views.py
from django.test import Client
from django.urls import reverse, resolve

import pytest
from pytest_django.asserts import assertTemplateUsed

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

    client.post("/user/signup/", credentials)
    
    client.post("/user/login/", {"username" : "testuser", "password" : "TestPassword"})    

    response = client.get(reverse("favourite-products"))

    assert response.status_code == 200
    
    assertTemplateUsed(response, 'favourite_product.html')
    