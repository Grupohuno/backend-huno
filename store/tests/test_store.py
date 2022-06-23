import json
from urllib import response
import pytest
from rest_framework.test import APIClient
from store.models import Store, Category, Product, Price

@pytest.fixture
def client():
    return APIClient()

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
    return {'store': store, 'category': category, 'product': product}

@pytest.mark.django_db
class TestApi():
    def test_dummy_endpoint(self, client):
        response = client.get("/api/dummy/")
        assert response.status_code == 200

    def test_get_products(self, client):
        response = client.get("/api/v1/products/")
        assert response.status_code == 200
        data = response.json()
        assert len(data['results']) == 1

    def test_get_products_category(self, client):
        response = client.get("/api/v1/products/category/C1")
        assert response.status_code == 200
        data = response.json()
        assert len(data['results']) == 1

    def test_get_product(self, client, seed_db):
        product_id = seed_db['product'].id
        response = client.get(f"/api/v1/products/{product_id}")
        assert response.status_code == 200

    def test_update_products(self, client):
        response = client.post('/api/v1/update-products/', {
            'store': 'Store1',
            'products_list': [{
                'name': 'P2',
                'store': 'Store1',
                'category': 'C1',
                'sku': 'hola',
                'brand': 'bestbrand',
                'size': 10,
                'image_url': 'www.image.cl',
                'page_url': 'www.buypage.cl',
                'price': 10000
            }]
        }, format='json')
        assert response.status_code == 200
        assert response.json()['error_products'] == []

    def test_search(self, client):
        response = client.get('/api/v1/product-search/', {'keyword': 'beeer'})
        assert response.status_code == 200
        assert len(response.json()['results']) == 1

    def test_search_not_found(self, client):
        response = client.get('/api/v1/product-search/', {'keyword': 'not found keyword'})
        assert response.status_code == 404
