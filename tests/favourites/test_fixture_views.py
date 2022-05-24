from django.test import Client
from django.urls import reverse, resolve

import pytest
from pytest_django.asserts import assertTemplateUsed

client = Client()

# Préparation
@pytest.fixture
def fixture_favourite_product_list_view():
    credentials = {
        'first_name' : 'Test',
        'last_name' : 'User',
        'username' : 'testuser',
        'email' : 'testuser@testing.com',
        'password1' : 'TestPassword',
        'password2' : 'TestPassword'
    }

    return credentials
    
@pytest.mark.django_db
def test_with_fixture_favourite_product_list_view(fixture_favourite_product_list_view):

    # Action
    client.post("/user/signup/", fixture_favourite_product_list_view)
    client.post("/user/login/", {"username" : "testuser", "password" : "TestPassword"})    
    response = client.get(reverse("favourite-products"))


    # Assertion
    assert response.status_code == 200
    assertTemplateUsed(response, 'favourite_product.html')
