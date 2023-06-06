from ..models.product import Product
from ..models.provider import Provider
from django import forms


class ProductForm(forms.ModelForm):
    provider = forms.ModelChoiceField(
        queryset=Provider.objects.all(),
        empty_label="Selecciona un proveedor",
        widget=forms.Select(
            attrs={
                "class": "form-control",
            }),
    )

    class Meta:
        model = Product
        fields = ["name", "price", "stock", "provider"]
        labels = {
            "name": "Nombre",
            "price": "Precio",
            "stock": "Stock",
            "provider": "Proveedor",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre"}
            ),
            "price": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Precio"}
            ),
            "stock": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Stock"}
            ),
        }
