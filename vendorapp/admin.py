from django.contrib import admin
from .models import Consignment
from vendorapp.models import Vendor_Account
# Register your models here.
admin.site.register(Vendor_Account)
admin.site.register(Consignment)
