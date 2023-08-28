from django.contrib import admin
from .models import Customer,Product,InwardPayments,AdminProfile,NewInvoice,ProductDetails

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(InwardPayments)
admin.site.register(AdminProfile)
admin.site.register(NewInvoice)
admin.site.register(ProductDetails)
