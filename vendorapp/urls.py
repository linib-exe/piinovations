from django.contrib import admin
from django.urls import path,reverse
from . import views

urlpatterns = [
    path('vendor_add_consignment/', views.vendor_add_consignment,name='vendorhome'),
    path('vendor_consignment_list/', views.vendor_consignment_list,name='consignmentlist'),
    path('vendor_delete_consignment/<int:id>', views.vendor_delete_consignment,name='deleteconsignment'),
    path('vendor_update_consignment/<int:id>', views.vendor_update_consignment,name='updateconsignment'),
    path('login/', views.login,name='login'),
]