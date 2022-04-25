import pytest
from rest_framework.test import APIClient, APITestCase

class StoreTests(APITestCase):
    def test_dummy_endpoint(self):
        client = APIClient()
        response = client.get('/api/dummy/', HTTP_ACCEPT='application/json')
        assert response.status_code == 200
