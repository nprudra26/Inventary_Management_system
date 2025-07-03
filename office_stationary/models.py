from django.db import models

# Create your models here.
from django.db import models

class OfficeStationary(models.Model):
    product_name = models.CharField(max_length=100)
    purchase_date = models.DateField()
    activation_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    mail_id = models.CharField(max_length=50,null=True, blank=True)
    warranty_years = models.PositiveIntegerField(help_text="How many years of warranty does this product have?")
    make_in = models.CharField(max_length=100, help_text="Model name or company name")

    def __str__(self):
        return f"{self.product_name} ({self.make_in})"
