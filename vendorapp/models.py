from django.db import models
from django.contrib.auth.models import User

# Create your models here.   

class Consignment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    consignee_name = models.CharField(max_length=200)
    consignee_address = models.CharField(max_length=200)
    consignee_phone = models.CharField(max_length=10)
    consignment_est_wt = models.FloatField()
    consignment_value = models.FloatField()
    consignment_payment_choices = [
        ('COD', 'COD'),
        ('Pre', 'Pre-Payment')
    ]
    consignment_payment_type = models.CharField(max_length=20, choices=consignment_payment_choices)
    # consignment_id = models.CharField(max_length=30, unique=True,null=True,blank=True)

    # def save(self,*args,**kwargs):
    #     if self.consignment_id is None:
    #         self.consignment_id = f'MI-{self.id}-{self.consignee_address}'
    #     super().save(*args,**kwargs)

    # def __str__(self):
    #     return self.consignment_id

    consignment_id = models.CharField(max_length=30, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the instance first to populate the id field
        if self.consignment_id is None:
            self.consignment_id = f'MI-{self.id}-{self.consignee_address}'
            self.save(update_fields=['consignment_id'])  # Save again to update the consignment_id field

    def __str__(self):
        return self.consignment_id
    
class Vendor_Account(models.Model):
    vendor_firstname = models.CharField(max_length=200)
    vendor_lastname = models.CharField(max_length=200)
    vendor_username = models.CharField(max_length=20)
    vendor_password = models.CharField(max_length=50)
    vendor_address = models.CharField(max_length=50)
    vendor_contact1 = models.CharField(max_length=10,unique=True)
    vendor_contact2 = models.CharField(max_length=10,blank=True,null=True)
    vendor_id = models.CharField(max_length=20,unique=True,null=True,blank=True)
    is_active = models.BooleanField(default=True,blank=True,null=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the instance first to populate the id field
        if self.vendor_id is None:
            self.vendor_id = f'MI-{self.id}-{self.vendor_address}'
            self.save(update_fields=['vendor_id'])  # Save again to update the consignment_id field

    def __str__(self):
        return self.vendor_id


