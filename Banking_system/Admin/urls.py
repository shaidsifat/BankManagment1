from django.contrib import admin
from django.urls import path
from Admin import views  

urlpatterns = [  
    
    path('index/', views.admin),  
   
]  