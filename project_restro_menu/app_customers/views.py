from django.shortcuts import render
from app_customers.models import Customer_info
from app_customers.forms import CustomerCreateForm

# Create your views here.
def show_customer(request):
    customer_list = Customer_info.objects.all()
    context = {'data':customer_list}
    return render(request, 'customers/show.html',context)

def create_customer(request):
    customer_create_form = CustomerCreateForm()
    context = {"customer_create_form": customer_create_form,
               'title':"Create Customers Here..."}
    
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        customer_contact = request.POST.get('customer_contact')
        customer_address = request.POST.get('customer_address')

        customer_obj = Customer_info()
        customer_obj.customer_name = customer_name
        customer_obj.customer_contact = customer_contact
        customer_obj.customer_email = customer_email
        customer_obj.customer_address = customer_address
        customer_obj.save()

    return render(request,'customers/create.html',context)
    



