from django.db import models

# Create your models here.

class Shop(models.Model):
    name= models.ForeignKey('khataapp.User', ondelete= models.CASCADE, blank= True, null= True)
    shop_name= models.CharField()
    address= models.CharField(max_length=250, null=True, blank=True)
    type_of_business = models.CharField(max_length=250, null=True, blank=True)

     def __str__(self):
		return self.name

