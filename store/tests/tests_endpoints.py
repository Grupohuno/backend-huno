import pytest
from rest_framework.test import APIClient, APITestCase


@pytest.mark.django_db
class StoreTests(APITestCase):
    client = APIClient()

    def test_dummy_endpoint(self):
        response = self.client.get("/api/dummy/", HTTP_ACCEPT="application/json")
        assert response.status_code == 200

    def test_products_endpoint(self):
        response = self.client.get("/api/v1/products/", HTTP_ACCEPT="application/json")
        assert response.status_code == 200
    
    def test_products_category_endpoint(self):
        response_1 = self.client.get("/api/v1/products/cerveza", HTTP_ACCEPT="application/json")
        response_2 = self.client.get("/api/v1/products/pisco", HTTP_ACCEPT="application/json")
        response_3 = self.client.get("/api/v1/products/bebida", HTTP_ACCEPT="application/json")
        assert response_1.status_code == 404
        assert response_2.status_code == 404
        assert response_3.status_code == 404

