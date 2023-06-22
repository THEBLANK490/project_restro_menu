from django.contrib import admin
from app_customers.models import Customer_info

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["customer_name","customer_email","customer_contact","customer_address"]
    search_fields = ['customer_name','customer_email']
    list_filter = ['customer_name',]

admin.site.register(Customer_info, CustomerAdmin)
