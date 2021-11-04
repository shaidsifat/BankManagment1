from django.shortcuts import render
from .models import Customer_info,Bank
from .models import Bank_Branch,Account, Loan

# Create your views here.
def admin(request):

 d1 = Customer_info.objects.all()
 print(d1)
 d2 = Customer_info.objects.get(address=Dhaka)
