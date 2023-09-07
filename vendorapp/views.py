from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Consignment

# Create your views here.
def vendor_add_consignment(request):
    if request.method == 'POST':
        consignee_name = request.POST.get('consignee_name')
        consignee_address = request.POST.get('consignee_address')
        consignee_phone = request.POST.get('consignee_phone')
        consignment_est_wt = request.POST.get('consignment_est_wt')
        consignment_value = request.POST.get('consignment_value')
        consignment_payment_type = request.POST.get('consignment_payment_type')
        consignment = Consignment(consignee_name=consignee_name,consignee_address=consignee_address,consignee_phone=consignee_phone,consignment_est_wt=consignment_est_wt,consignment_value=consignment_value,consignment_payment_type=consignment_payment_type)
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