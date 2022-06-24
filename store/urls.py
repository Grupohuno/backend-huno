from django.urls import path
from .views import DummyView, ProductsView, CategoryView, ProductView, UpdateProductsView, FilterProductsView, NonPaginateProductsView,NonPaginateFilterProductsView

urlpatterns = [
    path("dummy/", DummyView.as_view()),
    path("v1/products/", ProductsView.as_view()),
    path("v1/products/category/<str:category>", CategoryView.as_view()),
    path("v1/products/<int:product_id>", ProductView.as_view()),
    path("v1/update-products/", UpdateProductsView.as_view()),
    path("v1/product-search/", FilterProductsView.as_view()),
    path("v1/np/products/", NonPaginateProductsView.as_view()),
    path("v1/np/product-search/", NonPaginateFilterProductsView.as_view()),
    path("v1/np/products/<int:product_id>", ProductView.as_view()),
]
