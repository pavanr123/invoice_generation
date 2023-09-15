from django.urls import path
from .views import otp , login , dashboard, addcoustmer, viewcoustmer, addProduct,viewProduct,editProduct,updateProduct,deleteProduct,addInwardPayments,viewInwardpayments,adminprofile,editadmin,createinvoice,viewinvoice,invoiceslip
from .views import editInvoice,deleteInvoice,deleteadmin,updateadmin,productdetails,AddUser,ViewUser,DeleteUser

urlpatterns = [
    path("otp" ,otp, name='otp'),
    path('login/',login,name='login'),
    path('dashboard',dashboard,name='dashboard'),
    path('addcoustmer',addcoustmer, name='addcoustmer'),  #completed
    path('viewcoustmer',viewcoustmer, name='viewcoustmer'), #completed
    path('addproduct',addProduct, name='addproduct'),    #completed
    path('viewproduct',viewProduct, name='viewproduct'), #completed
    path('editproduct/<int:id>',editProduct, name='editProduct'),
    path('updateProduct/<int:id>',updateProduct, name='updateProduct'),
    path('deleteProduct/<int:id>',deleteProduct, name='deleteProduct'),     #completed
    path('addinwardpayments',addInwardPayments, name='addinwardpayments'),   #completed
    path('viewinwardpayments',viewInwardpayments, name='viewinwardpayments'), #completd
    path('adminprofile',adminprofile, name='adminprofile'),  #completed
    path('editadmin',editadmin, name='editadmin'),
    path('deleteadmin/<int:id>',deleteadmin, name='deleteadmin'), #completed
    path('updateadmin/<int:id>',updateadmin, name='updateadmin'), 
    path('createinvoice/',createinvoice, name='createinvoice'), # facing an error
    path('viewinvoice',viewinvoice, name='viewinvoice'),   #completed
    path('editinvoice/<int:id>',editInvoice, name='editInvoice'),
    path('deleteinvoice/<int:id>',deleteInvoice, name='deleteInvoice'), #completed
    path('invoiceslip/<int:id>',invoiceslip, name='invoiceslip'), #completed
    path('productdetails',productdetails, name='productdetails'),
    path('adduser',AddUser,name="AddUser"),                 #completed    
    path('viewusers',ViewUser,name="ViewUser"),             #completed
    path('deleteuser/<int:id>',DeleteUser,name="DeleteUser"), #completed 
]
