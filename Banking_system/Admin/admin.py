from django.contrib import admin
from .models import Customer_info,Bank, Bank_Branch,Account,Loan


class   Customer_Admininfo(admin.ModelAdmin):
    list_display = ('id','phone','address')
    list_filter = (
        
       'id',
       'phone',
       'address',
    )
    search_fields = ('id',)


class  Bank_Admin(admin.ModelAdmin):
    list_display = ('id','Bank_name')
    search_fields = ('Bank_name','code','address')

admin.site.register(Account)
admin.site.register(Loan)
admin.site.register(Bank, Bank_Admin)
admin.site.register(Customer_info, Customer_Admininfo)
admin.site.register(Bank_Branch)


