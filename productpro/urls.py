from django.urls import path
from .views import provider_views

urlpatterns = [
    path("provider/new", provider_views.provider_create, name="provider-create"),
    path("provider-list", provider_views.provider_list, name="provider-list"),
    path("provider/<int:pk>/delete", provider_views.provider_delete, name="provider-delete"),
]
