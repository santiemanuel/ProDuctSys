from ..models.provider import Provider
from django import forms


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ["first_name", "last_name", "personal_id"]
        labels = {
            "first_name": "Nombre",
            "last_name": "Apellido",
            "personal_id": "DNI",
        }
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Apellido"}
            ),
            "personal_id": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "DNI"}
            ),
        }
