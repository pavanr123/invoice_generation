from xml.dom.minidom import parseString
from django.db import models
from django.utils import timezone


# Create your models here.
class Customer(models.Model):
    customer = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100)
    mail_id = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=100)
    gst_number = models.CharField(max_length=100,default="None")
    state_code = models.CharField(max_length=100)
    
    def __str__(self):
        return self.customer


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_cost =  models.CharField(max_length=100)
    hsn_no = models.CharField(max_length=100)
    cgst = models.CharField(max_length=100,default=0)
    sgst = models.CharField(max_length=100,default=0)
    igst = models.CharField(max_length=100,default=0)

    def __str__(self):
        return self.product_name
    


class InwardPayments(models.Model):
    customer_name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_name
    


class AdminProfile(models.Model):
    client = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    mail_id = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    pan_number = models.CharField(max_length=100)
    gst_number = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    bank_branch = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=100)

    def __str__(self):
        return self.client
    
    
class NewInvoice(models.Model):
    client_name = models.CharField(max_length=100)
    purchase_order_number = models.CharField(max_length=100)
    vendor_code = models.CharField(max_length=100)
    invoice_date = models.DateField()
    invoice_no = models.CharField(max_length=100)

    def __str__(self):
        return self.client_name


class ProductDetails(models.Model):
    invoice = models.ForeignKey(NewInvoice, on_delete=models.CASCADE)
    purchase_id = models.CharField(max_length=100)
    purchase_date = models.DateField()
    no_of_units_allowed = models.PositiveIntegerField()
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.invoice


class Users(models.Model):
     username = models.CharField(max_length=100)
     email = models.CharField(max_length=100)
     password = models.CharField(max_length=100)
     role = models.CharField(max_length=100)
     creation_time = models.DateTimeField(default=timezone.now)
     status = models.CharField(max_length=100)

     def __str__(self):
         return self.username







# class NewInvoice(models.Model):
#     client_name = models.CharField(max_length=100)
#     purchase_order_number = models.CharField(max_length=100)
#     vendor_code = models.CharField(max_length=100)
#     invoice_date = models.CharField(max_length=100)
#     purchase_id = models.CharField(max_length=100)
#     purchase_date = models.CharField(max_length=100)
#     no_of_units_allowed = models.CharField(max_length=100)
#     cost_per_unit = models.CharField(max_length=100)
#     invoice_no = models.CharField(max_length=100)

#     def __str__(self):
#         return self.client_name


# class InvoiceProductDetails(models.Model):
#     product_id = models.CharField(max_length=100)
#     purchase_date = models.CharField(max_length=100)
#     no_of_units_allowed = models.CharField(max_length=100)
#     cost_per_unit = models.CharField(max_length=100)

#     def __str__(self):
#         return self.product_id
