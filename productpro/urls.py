from django.urls import path
from .views import provider_views
from .views import product_views

urlpatterns = [
    path("provider/new", provider_views.provider_create, name="provider-create"),
    path("provider-list", provider_views.provider_list, name="provider-list"),
    path("provider/<int:pk>/delete", provider_views.provider_delete, name="provider-delete"),
    path("product/new", product_views.product_create, name="product-create"),
    path("product-list", product_views.product_list, name="product-list"),
    path("product/<int:pk>/delete", product_views.product_delete, name="product-delete"),
]
