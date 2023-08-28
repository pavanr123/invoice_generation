from django.urls import path
from .views import otp , login , dashboard, addcoustmer, viewcoustmer, addProduct,viewProduct,editProduct,updateProduct,deleteProduct,addInwardPayments,viewInwardpayments,adminprofile,editadmin,createinvoice,viewinvoice,invoiceslip
from .views import editInvoice,updateInvoice,deleteInvoice,deleteadmin,updateadmin,productdetails

urlpatterns = [
    path("otp" ,otp, name='otp'),
    path('login/',login,name='login'),
    path('dashboard',dashboard,name='dashboard'),
    path('coustmer',addcoustmer, name='coustmer'),
    path('viewcoustmer',viewcoustmer, name='viewcoustmer'),
    path('addproduct',addProduct, name='addproduct'),
    path('viewproduct',viewProduct, name='viewproduct'),
    path('editproduct/<int:id>',editProduct, name='editProduct'),
    path('updateProduct/<int:id>',updateProduct, name='updateProduct'),
    path('deleteProduct/<int:id>',deleteProduct, name='deleteProduct'),
    path('addinwardpayments',addInwardPayments, name='addinwardpayments'),
    path('viewInwardpayments',viewInwardpayments, name='viewInwardpayments'),
    path('adminprofile',adminprofile, name='adminprofile'),
    path('editadmin',editadmin, name='editadmin'),
    path('deleteadmin/<int:id>',deleteadmin, name='deleteadmin'),
    path('updateadmin/<int:id>',updateadmin, name='updateadmin'),
    path('createinvoice/',createinvoice, name='createinvoice'),
    path('viewinvoice',viewinvoice, name='viewinvoice'), 
    path('editinvoice/<int:id>',editInvoice, name='editInvoice'),
    path('updateinvoice/<int:id>',updateInvoice, name = 'updateInvoice'),
    path('deleteinvoice/<int:id>',deleteInvoice, name='deleteInvoice'),
    path('invoiceslip/<int:id>',invoiceslip, name='invoiceslip'),
    path('productdetails',productdetails, name='productdetails'),
]