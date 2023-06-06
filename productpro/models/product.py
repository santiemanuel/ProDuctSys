from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    provider = models.ForeignKey("Provider", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.price} - {self.stock} - {self.provider}"
