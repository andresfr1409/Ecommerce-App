from django.shortcuts import render
from Servicios.models import Servicio 

def home(request):
    
    return render(request,'Ecommerce/home.html')


