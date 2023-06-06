from django.shortcuts import render, redirect
from ..models.product import Product
from ..forms.product_form import ProductForm


def product_list(request):
    products = Product.objects.all()
    context = {
        "products": products,
        "title": "Lista de Productos",
    }
    return render(request, "product_list.html", context)


def product_create(request):
    form = ProductForm()
    context = {
        "form": form,
        "submit": "Crear",
        "title": "Crear Producto",
        "action": "btn-primary",
    }
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product-list")
    return render(request, "product_form.html", context)


def product_delete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect("product-list")