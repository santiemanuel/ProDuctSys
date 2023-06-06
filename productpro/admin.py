from django.contrib import admin
from .models.provider import Provider
from .models.product import Product


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    fields = ["first_name", "last_name", "personal_id"]
    list_display = ["first_name", "last_name", "personal_id"]
    search_fields = ["first_name", "last_name", "personal_id"]
    list_filter = ["first_name", "last_name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ["name", "price", "stock", "provider"]
    list_display = ["name", "price", "stock", "provider"]
    search_fields = ["name", "price", "stock", "provider"]
    list_filter = ["name", "price", "provider"]
