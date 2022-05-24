from django.urls import reverse, resolve
from favourites.views import FavouriteProductListView, markFavourtie

def test_favourite_products():

    url = reverse("favourite-products")
    assert resolve(url).view_name == 'favourite-products'
    assert resolve(url).func.view_class == FavouriteProductListView

def test_mark_favourites():
    url = reverse('mark-favourite',args=[3])
    assert resolve(url).view_name == 'mark-favourite'
    assert resolve(url).func == markFavourtie
