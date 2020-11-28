from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):

    Status_Choice = (
        ('ACTIVE', 'Active'),
        ('INACTIVE','Inactive')
    )

    type_choice= (
        ('USER','user'),
        ('STAFF','staff')
    )
    email = models.EmailField('email_address',unique=True)
    contact_number = models.TextField(max_length=10)
    #aadhar_card = models.TextField(max_length=12,blank=False)
    #address = models.TextField(max_length=60,blank=False)
    status = models.CharField(max_length=10,null=False,choices=Status_Choice,default='ACTIVE')
    type_c = models.CharField(max_length=10,null=False,choices=type_choice,default='USER')
    pincode = models.TextField(max_length=6, blank=False, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
# Create your models her e.

    def __str__(self):
        return self.email


