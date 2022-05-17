import pytest

from store.models import Store, Category, Product, Price


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
def test_create_product():
    store = Store.objects.create(name="Store1", web_url="www.store1.cl")
    category = Category.objects.create(name="C1")
    product = Product.objects.create(
        name="P1",
        store_id=store,
        category_id=category,
        sku="1234",
        description="description",
        size=9.1,
        size_metric="sm",
        image_url="www.image.cl",
        page_url="www.buypage.cl",
    )
    assert product.name == "P1"
    assert product.store_id.name == "Store1"
    assert product.category_id.name == "C1"
    assert product.sku == "1234"
    assert product.description == "description"
    assert product.size == 9.1
    assert product.size_metric == "sm"
    assert product.image_url == "www.image.cl"
    assert product.page_url == "www.buypage.cl"


@pytest.mark.django_db
def test_create_price():
    store = Store.objects.create(name="Store1", web_url="www.store1.cl")
    category = Category.objects.create(name="C1")
    product = Product.objects.create(
        name="P1",
        store_id=store,
        category_id=category,
        sku="1234",
        description="description",
        size=9.1,
        size_metric="sm",
        image_url="www.image.cl",
    )
    price = Price.objects.create(price=1990, date="2022-05-17", product_id=product)
    assert price.price == 1990
    assert price.date == "2022-05-17"
    assert price.product_id.name == "P1"
