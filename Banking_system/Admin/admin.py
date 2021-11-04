from django.contrib import admin

#Bank,Bank_Branch, Account, Loan
# Register your models here.
from .models import  Customer_info,Bank
from .models import Bank_Branch,Account,Loan

admin.site.register(Customer_info),
admin.site.register(Bank),
admin.site.register(Bank_Branch),
admin.site.register(Account),
admin.site.register(Loan)
