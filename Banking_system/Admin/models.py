from django.db import models

# Create your models here.






class Bank(models.Model):

    Bank_name = models.CharField(max_length=250)   
    code = models.IntegerField()
    address = models.CharField(max_length=250)


    def __str__(self):
        return self.Bank_name 


class Bank_Branch(models.Model):
   
    name = models.CharField(max_length=250)   
    Bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"

class Customer_info(models.Model):
 
    name = models.CharField(max_length=250)
    phone = models.TextField(max_length=100)
    address = models.CharField(max_length=250)
    Bank =  models.ForeignKey(Bank,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

class Account(models.Model):
    a_c_number = models.AutoField(primary_key=True)
    type = models.CharField(max_length=500)
    Balance = models.IntegerField()
    Customer_info = models.ForeignKey( Customer_info, on_delete=models.CASCADE)
    bank =  models.ForeignKey(Bank, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.a_c_number)

class Loan(models.Model):

    id =   models.AutoField(primary_key=True)
    type = models.CharField(max_length=500)
    amount = models.CharField(max_length=500)  
    browwer_field =  models.ForeignKey( Customer_info, on_delete=models.CASCADE)
  
    def __str__(self):
        return  str(self.pk)