from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

class Vregistro(View):
    
    def get(self, request):
        
        form_registro = UserCreationForm()
        
        return render(request,"Autenticacion/registro_usuario/registro.html", {'form_registro': form_registro})

    def post(self, request):
        
        form_registro = UserCreationForm(request.POST)
        
        if form_registro.is_valid():
            usuario = form_registro.save()
            
            login(request, usuario)
            
            return redirect('Home')
        else:
            for mensaje in form_registro.error_messages:
                messages.error(request, form_registro.error_messages[mensaje])
            return render(request,"Autenticacion/registro_usuario/registro.html", {'form_registro': form_registro})

def inicio_sesion(request):
    
    if request.method == 'POST':
        form_login = AuthenticationForm(request, request.POST)
        if form_login.is_valid():
            usuario = authenticate(request, username=form_login.cleaned_data['username'], password=form_login.cleaned_data['password'])
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
    else: 
        form_login = AuthenticationForm()
    
    return render(request,"Autenticacion/login/inicio_sesion.html", {'form_login': form_login})

def cerrar_sesion(request):
    
    logout(request)
    
    return redirect('Home')