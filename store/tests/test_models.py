# pylint: disable=W0621
import pytest

from store.models import Store, Category, Price


@pytest.mark.django_db
def test_create_store():
    store = Store.objects.create(name="Store1", web_url="www.store1.cl")
    assert store.name == "Store1"
    assert store.web_url == "www.store1.cl"


@pytest.mark.django_db
def test_create_category():
    category = Category.objects.create(name="C1")
    assert category.name == "C1"


@pytest.mark.django_db
def test_create_product(seed_db):
    product = seed_db["product"]
    assert product.name == "Searchable product beeer inside"
    assert product.store_id.name == "Store1"
    assert product.category_id.name == "C1"
    assert product.sku == "1234"
    assert product.brand == "brand"
    assert product.size == "330cc"
    assert product.image_url == "www.image.cl"
    assert product.page_url == "www.buypage.cl"


@pytest.mark.django_db
def test_create_price(seed_db):
    product = seed_db["product"]
    price = Price.objects.create(price=1990, date="2022-05-17", product_id=product)
    assert price.price == 1990
    assert price.date == "2022-05-17"
    assert price.product_id.name == "Searchable product beeer inside"
