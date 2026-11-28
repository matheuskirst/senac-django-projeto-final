from django.db import models

from .product import Product
from .facility import Facility

class StockLevel(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, to_field="sku", db_column="sku", on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=0)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["facility", "product"], name="unique_facility_product_sku"
            )
        ]

    def __str__(self):
        return f"{self.facility} | {self.product_name}: {self.quantity}"
