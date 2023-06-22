from django import forms
from app_customers.models import Customer_info

class CustomerCreateForm(forms.ModelForm):
    class Meta:
        fields = ("customer_name","customer_email",'customer_address','customer_contact')
        model = Customer_info