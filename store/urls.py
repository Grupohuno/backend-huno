from django.urls import path
from .views import DummyView, ProductsView, CategoryView, ProductView, UpdateProductsView, FilterProductsView

urlpatterns = [
    path("dummy/", DummyView.as_view()),
    path("v1/products/", ProductsView.as_view()),
    path("v1/products/<str:category>", CategoryView.as_view()),
    path("v1/product/<int:product_id>", ProductView.as_view()),
    path("v1/update-products/", UpdateProductsView.as_view()),
    path("v1/product-search/", FilterProductsView.as_view()),
]
