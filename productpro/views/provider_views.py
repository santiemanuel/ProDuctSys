from django.shortcuts import render, redirect
from ..models.provider import Provider
from ..forms.provider_form import ProviderForm


def provider_list(request):
    providers = Provider.objects.all()
    context = {
        "providers": providers,
        "title": "Lista de Proveedores",
    }
    return render(request, "provider_list.html", context)


def provider_create(request):
    form = ProviderForm()
    context = {
        "form": form,
        "submit": "Crear",
        "title": "Crear Proveedor",
        "action": "btn-primary",
    }
    if request.method == "POST":
        form = ProviderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("provider-list")
    return render(request, "provider_form.html", context)


def provider_delete(request, pk):
    provider = Provider.objects.get(id=pk)
    provider.delete()
    return redirect("provider-list")
