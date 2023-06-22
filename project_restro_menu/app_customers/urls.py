from django.urls import path
from app_customers import views

urlpatterns = [
     path("show/",views.show_customer, name='customer-show'),
     path('create/',views.create_customer,name='customer-create')
   
]
