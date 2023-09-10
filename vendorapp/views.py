from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Consignment,Vendor_Account
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

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
                                  consignment_payment_type=consignment_payment_type,
                                  user=request.user)
        consignment.save()

        return redirect('/vendor_consignment_list/')
    return render(request,'vendorhome.html')

@login_required(login_url='login')
def vendor_consignment_list(request):
    user = request.user
    consignmet = Consignment.objects.filter(user=user)
    # for x in consignmet:
    #     print(x.consignment_id)
    if request.method == 'POST':
        st = request.POST.get('search')
        print(st)
        if st!=None:
            consignmet = Consignment.objects.filter(Q(user=user),
                                                    Q(consignee_name__icontains=st)|
                                                    Q(consignment_id__icontains=st))                                
    return render(request,'consignmentlist.html',{'consignments':consignmet})

@login_required(login_url='login')
def vendor_delete_consignment(request,id):
    consignemnt = Consignment.objects.get(pk=id)
    if request.method=='POST':
        consignemnt.delete()
        return redirect('/vendor_consignment_list/')
    return render(request,'deleteAsk.html'  )

@login_required(login_url='login')
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
    
def loginVendor(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('consignmentlist')  # Redirect to the home page or any other desired URL
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def registerVendor(request):
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
                                vendor_address=address,
                                vendor_username=username,
                                vendor_password=password)
        vendor.save()
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login') 

    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('login')