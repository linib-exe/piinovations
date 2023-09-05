from django.shortcuts import render
from django.http import HttpResponse
from .models import Consignment

# Create your views here.
def vendorhome(request):
    if request.method == 'POST':
        consignee_name = request.POST.get('consignee_name')
        consignee_address = request.POST.get('consignee_address')
        consignee_phone = request.POST.get('consignee_phone')
        consignment_est_wt = request.POST.get('consignment_est_wt')
        consignment_value = request.POST.get('consignment_value')
        consignment_payment_type = request.POST.get('consignment_payment_type')
        consignment = Consignment(consignee_name=consignee_name,consignee_address=consignee_address,consignee_phone=consignee_phone,consignment_est_wt=consignment_est_wt,consignment_value=consignment_value,consignment_payment_type=consignment_payment_type)
        consignment.save()
    return render(request,'vendorhome.html')

