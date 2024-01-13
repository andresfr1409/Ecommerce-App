from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

class Vregistro(View):
    
    def get(self, request):
        
        form_registro = UserCreationForm()
        
        return render(request,"Autenticacion/registro.html", {'form_registro': form_registro})

    def post(self, request):
        
        form_registro = UserCreationForm(request.POST)
        
        if form_registro.is_valid():
            usuario = form_registro.save()
            
            login(request, usuario)
            
            return redirect('Home')
        else:
            for mensaje in form_registro.error_messages:
                messages.error(request, form_registro.error_messages[mensaje])
            return render(request,"Autenticacion/registro.html", {'form_registro': form_registro})
