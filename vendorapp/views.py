from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Consignment,Vendor_Account
from django.contrib.auth.models import User

# Create your views here.
def vendor_add_consignment(request):
    if request.method == 'POST':
        consignee_name = request.POST.get('consignee_name')
        consignee_address = request.POST.get('consignee_address')
        consignee_phone = request.POST.get('consignee_phone')
        consignment_est_wt = request.POST.get('consignment_est_wt')
        consignment_value = request.POST.get('consignment_value')
        consignment_payment_type = request.POST.get('consignment_payment_type')
        consignment = Consignment(consignee_name=consignee_name,
                                  consignee_address=consignee_address,
                                  consignee_phone=consignee_phone,
                                  consignment_est_wt=consignment_est_wt,
                                  consignment_value=consignment_value,
                                  consignment_payment_type=consignment_payment_type)
        consignment.save()
        return redirect('/vendor_consignment_list/')
    return render(request,'vendorhome.html')

def vendor_consignment_list(request):
    consignmet = Consignment.objects.all()
    return render(request,'consignmentlist.html',{'consignments':consignmet})

def vendor_delete_consignment(request,id):
    consignemnt = Consignment.objects.get(pk=id)
    consignemnt.delete()
    return redirect('/vendor_consignment_list/')

def vendor_update_consignment(request, id):
    consignment = Consignment.objects.get(pk=id)
    if request.method == 'POST':
        # Handle form submission
        consignment.consignee_name = request.POST.get('consignee_name')
        consignment.consignee_address = request.POST.get('consignee_address')
        consignment.consignee_phone = request.POST.get('consignee_phone')
        consignment.consignment_est_wt = request.POST.get('consignment_est_wt')
        consignment.consignment_value = request.POST.get('consignment_value')
        consignment.consignment_payment_type = request.POST.get('consignment_payment_type')
        consignment.save()
        return redirect('/vendor_consignment_list/')
    else:
        # Pre-fill form fields with existing values
        return render(request, 'vendorhome.html', {'consignment': consignment})
    
def login(request):
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        contact1 = request.POST.get('contact1')
        contact2 = request.POST.get('contact2')
        vendor = Vendor_Account(vendor_firstname=first_name,
                                vendor_lastname=last_name,
                                vendor_contact1=contact1,
                                vendor_contact2=contact2,
                                vendor_address=address,)
        vendor.save()
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login') 

    return render(request, 'register.html')