from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm

class Vregistro(View):
    
    def get(self, request):
        
        form_registro = UserCreationForm()
        
        return render(request,"Autenticacion/registro.html", {'form_registro': form_registro})

    def post(self, request):
        pass

