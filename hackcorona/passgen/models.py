from django.db import models
from django.utils import timezone

category_choices = ( 
    ("Essential Services Pass", "Essential Services Pass"), 
    ("Emergency Services Pass", "Emergency Services Pass"),   
) 
subcategory_choices = ( 
    ("ATM/Banking", "ATM/Banking"), 
    ("Delivery Worker", "Delivery Worker"),
    ("Fruit/Vegetable Vendor","Fruit/Vegetable Vendor"),
    ("Govt Officials","Govt Officials"),
    ("Grocery Vendor","Grocery Vendor"),
    ("Milk Vendor","Milk Vendor"),
    ("Health Worker","Health Worker"),
    ("IT/Tele Communication","IT/Tele Communication"),
    ("Municipal Services","Municipal Services"),
    ("Power/Electricity","Power/Electricity"),
    ("Sanitation","Sanitation"),
    ("Businessman","Businessman"),

) 

# Create your models here.
class PassModel(models.Model):
    district=models.CharField(max_length=20,null=True)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    vehiclenumber=models.CharField(max_length=200,null=True)
    phonenumber=models.CharField(max_length=10,null=True)
    aadharcardnumber=models.CharField(max_length=12,null=True)
    address=models.CharField(max_length=200,null=True)
    reason=models.CharField(max_length=200,null=True)
    issuedate=models.DateTimeField(default=timezone.now)
    passcategory=models.CharField(max_length=30,choices = category_choices) 
    subcategory=models.CharField(max_length=30,choices = subcategory_choices) 
    attachphoto=models.ImageField(upload_to='profile_pics')
    attachidproof=models.ImageField(upload_to='id_proof')
    uniquenumber=models.CharField(max_length=10000,default=201301)
    checked=models.BooleanField(default=0)
