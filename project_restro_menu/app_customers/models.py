from django.db import models

# Create your models here.
class Customer_info(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=100)
    customer_contact = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=100)

    class Meta:
        db_table = "Customer_info"
        ordering = ["-customer_name"]