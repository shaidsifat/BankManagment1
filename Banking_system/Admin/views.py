from django.shortcuts import render
from .models import Customer_info,Bank
from .models import Bank_Branch,Account,Loan

# Create your views here.
def admin(request):

 d1 = Customer_info.objects.all()
 print(d1)
 d2 = Customer_info.objects.filter(address="kalabagan")
 print(d2)
 d3 = Customer_info.objects.all().filter(id__lte=2) 
 d4 = Customer_info.objects.all().filter()[1:4]
 print(d3) 
 print(d4)
 d5 = Customer_info.objects.filter(Bank=1)
 print(d5) 
 d6 = Loan.objects.all().filter(amount__gte=5000)
 print(d6)
 d7 = Loan.objects.all().filter().values(address="kalabagan")