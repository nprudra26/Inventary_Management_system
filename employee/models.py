from django.db import models

class Employee(models.Model):
    #emp_id = models.CharField(max_length=20, primary_key=True)
    emp_name = models.CharField(max_length=50)
    #email = models.EmailField()
    handover_date = models.DateField(null=True, blank=True)
    model_name = models.CharField(max_length=50, blank=True)
    laptop_name = models.CharField(max_length=50, blank=True)
    processor = models.CharField(max_length=50, blank=True)
    windows = models.CharField(max_length=50, blank=True)
    ssd = models.CharField(max_length=20, blank=True)
    ram = models.CharField(max_length=20, blank=True)
    device_id = models.CharField(max_length=50, blank=True)
    product_serial_no = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=50, blank=True)
    hostname = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=100, blank=True)
    dlp = models.CharField(max_length=20, blank=True)
    
    OPTION_CHOICES = (
        ('Old', 'Old'),
        ('New', 'New'),
    )
    option_type = models.CharField(max_length=10, choices=OPTION_CHOICES, default='New')

    def __str__(self):
        return f"{self.emp_name} ({self.emp_id})"
