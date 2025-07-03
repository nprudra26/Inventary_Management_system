from django.db import models

# Create your models here.
from django.db import models

class Repair(models.Model):
    DEVICE_CHOICES = [
        ('Laptop', 'Laptop'),
        ('Offive TV','Office TV'),
        ('Mouse', 'Mouse'),
        ('Printer', 'Printer'),
        ('Monitor', 'Monitor'),
        ('Other', 'Other'),
    ]

    device_type = models.CharField(max_length=50, choices=DEVICE_CHOICES)
    emp_name = models.CharField(max_length=100)
    device_id = models.CharField(max_length=50)
    outward_date = models.DateField(null=True, blank=True)
    inward_date = models.DateField(null=True, blank=True)
    purpose_of_repair = models.TextField()
    client_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.device_type} - {self.device_id} - {self.emp_name}"
