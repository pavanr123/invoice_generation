#from asyncio.windows_events import NULL
from queue import Empty
from unittest import result
from django.shortcuts import render,redirect,HttpResponse
from .models import Customer, Product ,InwardPayments,AdminProfile,NewInvoice,ProductDetails
import random
from django.core.mail import send_mail
from django.conf import settings
import datetime
import json
from django.http import JsonResponse


# Create your views here.

def login(request):
    return render(request,'login.html')


def otp(request):
    db_email = "usmanbashap@pathbreakertech.com"
    db_password = "Invoice@!23"
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if email != db_email:
            return HttpResponse("invalid email")
        if password != db_password:
            return HttpResponse("invalid password")
        otp = str(random.randint(100000, 999999))
        try:
            send_mail(
                'OTP Verification',
                'Your OTP: '+ otp,
                # "usmanbashap@pathbreakertech.com",
                settings.EMAIL_HOST_USER,
                [email],
                False,
            )
        except Exception as e:
            print(e)

        request.session['otp'] = otp
        request.session['email'] = email
    return render(request, 'otp.html')


def dashboard(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        if otp == request.session.get('otp'):
            return render(request, 'dashboard.html')
            # return HttpResponse('OTP verified successfully!')
        else:
            # return render(request,'otp.html',{'result': 'Invalid OTP'})
            return HttpResponse('Invalid OTP')
        
    total_rows_count = NewInvoice.objects.all().count()
    total_cus = Customer.objects.all().count()

    result = {
        'total_rows_count':total_rows_count,
        'total_cus':total_cus,
    }
    return render(request,"dashboard.html",result)


def addcoustmer(request):
    if request.method == "POST":
        customer = request.POST['client']
        mobile_number = request.POST['mobile']
        mail_id = request.POST['email']
        address = request.POST['address']
        state = request.POST['state']
        city = request.POST['city']
        pin_code = request.POST['pincode']
        gst_number = request.POST['gst']
        state_code = request.POST['stateCode']

        add_cum = Customer(customer=customer,mobile_number=mobile_number,mail_id=mail_id,address=address,state=state,city=city,
                           pin_code=pin_code,gst_number=gst_number,state_code=state_code)
        
        add_cum.save()
        return redirect("/dashboard")
    elif request.method == "GET":
        return render(request,'coustmer.html')
    else:
        return HttpResponse("ERROR")


def viewcoustmer(request):
    if 'q' in request.GET:
        q = request.GET['q']
        customer = Customer.objects.filter(customer__icontains=q)
    else:

        customer = Customer.objects.all()
    result = {
        'customer': customer 
    }
    
    return render(request, 'viewcoustmer.html',result)


def addProduct(request):
    if request.method == "POST":
        product_name = request.POST['product_name']
        product_cost = request.POST['productcost']
        hsn_no = request.POST['hsn_no']
        cgst = request.POST['cgst']
        sgst= request.POST['sgst']
        igst = request.POST['igst']
        #custermer_id = req.[cy'']

        add_product = Product(product_name=product_name,product_cost=product_cost,hsn_no=hsn_no,cgst=cgst,sgst=sgst,igst=igst)
        
        add_product.save()
        return redirect("/dashboard")
    elif request.method == "GET":
        # //user_details = users.find_by_role(role=admin)
        # user_id = user_details.user_id
        # user_id = user_id
        return render(request,'addproduct.html')
    else:
        return HttpResponse("ERROR")
    

def viewProduct(request):
    if 'q' in request.GET:
        q = request.GET['q']
        # customer = Customer.objects.filter(customer__icontains=q)
        product = Product.objects.filter(product_name__icontains=q)
    else:
        product = Product.objects.all()
    result = {
    'product': product
    }
    return render(request ,'viewproduct.html',result)


def editProduct(request,id):
    product = Product.objects.get(id=id)
    return render(request,'editproduct.html',{"product":product})


def updateProduct(request,id):
    if request.method == "POST":
        product_name = request.POST['product_name']
        product_cost = request.POST['productcost']
        hsn_no = request.POST['hsn_no']

        product = Product.objects.get(id=id)

        product.product_name = product_name
        product.product_cost = product_cost
        product.hsn_no = hsn_no
        product.save()
        return redirect("/viewproduct")
    return HttpResponse("ERROR")


def deleteProduct(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("/viewproduct")


def addInwardPayments(request):
    if request.method == "POST":
        customer_name = request.POST['client']
        amount = request.POST['amount']
        date = request.POST['date']

        add_inward = InwardPayments(customer_name = customer_name,amount = amount,date = date)
        
        add_inward.save()
        return redirect("/dashboard")
    elif request.method == "GET":
        return render(request,'addInwardPayments.html')
    else:
        return HttpResponse("ERROR")


def viewInwardpayments(request):
    view = InwardPayments.objects.all()
    result = {
        'view': view
    }
    return render(request ,'viewInwardpayments.html',result)



def adminprofile(request):
    if request.method == "POST":
        client = request.POST['client']
        gender = request.POST['gender']
        mail_id = request.POST['email']
        address = request.POST['address']
        state = request.POST['state']
        phone_number = request.POST['phone']
        company_name = request.POST['company']
        pan_number = request.POST['pan']
        gst_number = request.POST['gst']
        account_number = request.POST['bankAccount']
        bank_name = request.POST['bankName']
        bank_branch = request.POST['bankBranch']
        ifsc_code = request.POST['ifsc']

        add_admin = AdminProfile(client=client,gender=gender,mail_id=mail_id,address=address,state=state,phone_number=phone_number,
                                 company_name=company_name,pan_number=pan_number,gst_number=gst_number,account_number=account_number,bank_name=bank_name,bank_branch=bank_branch,
                                 ifsc_code=ifsc_code)
        
        add_admin.save()
        return redirect('/dashboard')
    elif request.method == "GET":
        return render(request,'adminprofile.html')
    else:
        return HttpResponse("ERROR")



def editadmin(request):
    admin_profiles = AdminProfile.objects.all()
    return render(request, 'editadmin.html',{'admin':admin_profiles})


def updateadmin(request,id):
    if request.method == "POST":
        client  = request.POST['client']
        gender = request.POST['gender']
        mail_id = request.POST['email']
        address = request.POST['address']
        state = request.POST['state']
        phone_number = request.POST['phone']
        company_name = request.POST['company']
        pan_number = request.POST['pan']
        gst_number = request.POST['gst']
        account_number = request.POST['bankAccount']
        bank_name = request.POST['bankName']
        bank_branch = request.POST['bankBranch']
        ifsc_code = request.POST['ifsc']

        admin = AdminProfile.objects.get(id=id)

        admin.client=client
        admin.gender=gender
        admin.mail_id=mail_id
        admin.address=address
        admin.state=state
        admin.phone_number=phone_number
        admin.company_name=company_name
        admin.pan_number=pan_number
        admin.gst_number=gst_number
        admin.account_number=account_number
        admin.bank_name=bank_name
        admin.bank_branch=bank_branch
        admin.ifsc_code=ifsc_code
        admin.save()
        return redirect("/editadmin")
    return HttpResponse("ERROR")


def deleteadmin(request,id):
    admin = AdminProfile.objects.get(id=id)
    admin.delete()
    return redirect("/dashboard")


def createinvoice(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            print(data)
            # Extract invoice data
            customer_name = data['customer_name']
            purchase_order_number = data['purchase_order']
            vendor_code = data['vendor_code']
            invoice_date = data['invoice_date']
            invoice_number = data['invoice_number']

            # Create NewInvoice instance
            new_invoice = NewInvoice.objects.create(
                client_name=customer_name,
                purchase_order_number=purchase_order_number,
                vendor_code=vendor_code,
                invoice_date=invoice_date,
                invoice_no=invoice_number
            )

            # Extract and save product details
            product_details = data['product_details']
            for detail in product_details:
                purchase_id = detail['product_id']
                purchase_date = detail['purchase_date']
                no_of_units_allowed = detail['no_of_units']
                cost_per_unit = detail['cost_per_unit']

                # Create and save product detail object
                product_details = ProductDetails(
                    invoice=new_invoice,
                    purchase_id=purchase_id,
                    purchase_date=purchase_date,
                    no_of_units_allowed=no_of_units_allowed,
                    cost_per_unit=cost_per_unit
                )
                product_details.save()

            return JsonResponse({"message": "Invoice created successfully!"})
        
        elif request.method == "GET":
            data = NewInvoice.objects.all().count()
            today = datetime.datetime.now()
            year1 = today.year
            year = str(year1)
            year = year[2:]
            add  = int(data) + 1
            invoice_no_gen = "INV/{year}/{add}".format(add = add,year=year)

            data = Customer.objects.all().values('customer')
            product_data = Product.objects.all().values('product_name','hsn_no')
            result = {
                'invoice_no_gen': invoice_no_gen,
                'data':data,
                'product_data':product_data
                        }
            return render(request,"createinvoice.html",result)
    
        # else:
        #     return HttpResponse("ERROR")  
        return render(request, 'createinvoice.html')
    except Exception as e:
        return JsonResponse({"success": f"data successfully saved: {e}"}, status=200)
        

def viewinvoice(request):
    invoice = NewInvoice.objects.all()
    result = {
        'invoice': invoice
    }
    return render(request ,'viewinvoice.html',result) 
 
    
def editInvoice(request,id):
    product = NewInvoice.objects.get(id=id)
    return render(request,'editinvoice.html',{"product":product})


def updateInvoice(request,id):
    if request.method == "POST":
        client_name = request.POST['client_name']
        purchase_order_number = request.POST['purchase_order']
        vendor_code = request.POST['vendor_code']
        invoice_date = request.POST['invoice_date']
        purchase_id = request.POST['purchase_id']
        purchase_date = request.POST['purchase_date']
        no_of_units_allowed = request.POST['units_allotted']
        cost_per_unit = request.POST['cost_per_unit']
        invoice_no = request.POST['invoice_number']

        invoice_update = NewInvoice.objects.get(id=id)

        invoice_update.client_name  = client_name
        invoice_update.purchase_order_number = purchase_order_number
        invoice_update.vendor_code = vendor_code
        invoice_update.invoice_date = invoice_date
        invoice_update.purchase_id = purchase_id
        invoice_update.purchase_date = purchase_date
        invoice_update.no_of_units_allowed = no_of_units_allowed
        invoice_update.cost_per_unit = cost_per_unit
        invoice_update.invoice_no = invoice_no
        invoice_update.save()

        return redirect("/viewinvoice")
    return HttpResponse("ERROR")


def deleteInvoice(request,id):
    invoice = NewInvoice.objects.get(id=id)
    invoice.delete()
    return redirect("/viewinvoice")


def invoiceslip(request,id): 
    data = AdminProfile.objects.all().values('bank_name','gst_number','pan_number','account_number','ifsc_code','state').first()
    bank_name = data['bank_name']
    gst_number = data['gst_number']
    pan_number = data['pan_number']
    account_number = data['account_number']
    ifsc_code = data['ifsc_code']
    admin_state = data['state']


    data = NewInvoice.objects.filter(id = id).values('client_name','invoice_no','invoice_date','purchase_order_number').first()
    purchase_order_number = data['purchase_order_number']
    invoice_no = data['invoice_no']
    invoice_date = data['invoice_date']
    client_name = data['client_name']

    # data = Product.objects.filter(hsn_no = purchase_order_number).values('product_name','product_cost','hsn_no').first()
    # product_name = data['product_name']
    # product_cost = data['product_cost']
    # hsn_no = data['hsn_no']

    

    data = Customer.objects.filter(customer = client_name).values('customer','mail_id','mobile_number','gst_number','state','address','state_code').first()
    customer = data['customer']
    mail_id = data['mail_id']
    mobile_number = data['mobile_number']
    cos_gst_number = data['gst_number']
    state = data['state']
    address = data['address']
    state_code = data['state_code']
   
    db_productdetails = ProductDetails.objects.filter(invoice_id=id).values('no_of_units_allowed','cost_per_unit','purchase_id')
    count = 1
    productdetails = []
    total = 0
    for db_productdetail in db_productdetails:
        no_of_units_allowed = db_productdetail['no_of_units_allowed']
        cost_per_unit = db_productdetail['cost_per_unit']
        amount = int(no_of_units_allowed) * int(cost_per_unit)
        purchase_id = db_productdetail['purchase_id']
        product_name = ""
        data = Product.objects.filter(hsn_no = purchase_id).values('product_name').first()
        if data:
            product_name = data['product_name']
        productdetail = {
            'no_of_units_allowed':db_productdetail['no_of_units_allowed'],
            'cost_per_unit': db_productdetail['cost_per_unit'],
            'purchase_id': purchase_id,
            'amount': amount,
            "product_name": product_name,
            'count':count
        }
        total = total + amount
        productdetails.append(productdetail)
        count = count + 1
    # import pdb; pdb.set_trace()

    
    sgst, cgst, igst = 0, 0, 0
    if state == admin_state:
        sgst = 9
        cgst = 9
    elif len(cos_gst_number) == 0:
         igst = 0      
    else:
        igst = 18

    total = round(total + (total * sgst/100) + (total * cgst/100) + (total * igst/100),2)
    
    result = {
        'customer': customer,
        'mail_id': mail_id,
        'mobile_number':mobile_number,
        'cos_gst_number':cos_gst_number,
        'state': state,
        'address':address,
        # 'product_name':product_name,
    #     'product_cost':product_cost,
    #     'hsn_no':hsn_no,
        'bank_name':bank_name,
        'gst_number':gst_number,
        'pan_number':pan_number,
        'account_number':account_number,
        'ifsc_code':ifsc_code,
        'invoice_date':invoice_date,
        'invoice_no':invoice_no,

        'sgst':sgst,
        'cgst':cgst,
        'igst':igst,
        'total':total,
        'state_code': state_code,
        # 'no_of_units_allowed':no_of_units_allowed,
        # 'cost_per_unit':cost_per_unit,
        'productdetails': productdetails,
        # 'count': count
    }
    return render(request, 'invoiceslip.html',result)


def productdetails(request):
    db_product_data = Product.objects.all().values('product_name','hsn_no')
    product_data = []

    for db_product in db_product_data:
        data = {
            "product_name": db_product['product_name'],
            "hsn_no": db_product['hsn_no'],
        }
        product_data.append(data)
    
    return JsonResponse({'data': product_data})

    



