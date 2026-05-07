from django.db import models

# Create your models here.

class CategoryServices(models.Model):
    services_id=models.BigIntegerField()
    services_name=models.CharField(max_length=100)
    services_price=models.BigIntegerField()
    
    def __str__(self):
        return f"{self.services_id}"  
    
    
class Services(models.Model):
    book_id = models.AutoField(primary_key=True) 
    first_name=models.CharField(max_length=100, blank=True, null=True)
    middle_name=models.CharField(max_length=100, blank=True, null=True)
    last_name=models.CharField(max_length=100, blank=True, null=True)
    company_name=models.CharField(max_length=100, blank=True, null=True)
    email=models.EmailField(blank=True,null=True)
    phonenumber=models.BigIntegerField(blank=True,null=True)
    address=models.CharField(max_length=100, blank=True, null=True)
    
    date=models.DateField( )
    time=models.TimeField( )
    start=models.CharField(max_length=10)
    finish=models.CharField(max_length=10)
    remove=models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.book_id}"
         
class ChooseServices(models.Model):
    chebook_id = models.ForeignKey(Services, on_delete=models.CASCADE)
    cheservices_id = models.ForeignKey(CategoryServices, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.chebook_id},{self.cheservices_id}"

    