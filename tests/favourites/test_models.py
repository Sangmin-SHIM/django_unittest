
from favourites.models import FavouriteProduct

from users.models import User
from products.models import Product

import secrets
import pytest

@pytest.mark.django_db
def test_favourite_product():


    product = Product.objects.create(
        name = secrets.token_hex(5),
        image = secrets.token_hex(10),
        description = secrets.token_hex(50),
        price=30
    )

    user = User.objects.create(
        username = secrets.token_hex(10),
        password = secrets.token_hex(20)
    )

    favProd = FavouriteProduct.objects.create(
        product = product,
        user = user
    )

    assert str(favProd) == f"product {product.name} by {user.get_full_name()}"