import pytest
from store.models import Store, Category, Product

@pytest.fixture(autouse=True)
@pytest.mark.django_db
def seed_db():
    store = Store.objects.create(name="Store1", web_url="www.store1.cl")
    category = Category.objects.create(name="C1")
    product = Product.objects.create(
        name="Searchable product beeer inside",
        store_id=store,
        category_id=category,
        sku="1234",
        brand="brand",
        size="330cc",
        image_url="www.image.cl",
        page_url="www.buypage.cl",
    )
    return {"store": store, "category": category, "product": product}

