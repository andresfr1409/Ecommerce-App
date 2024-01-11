from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from proyectoWebEcommerce.settings import EMAIL_HOST_USER
from .forms import FormularioContacto

def contacto(request):
    
    if request.method == 'POST':
        formulario_contacto = FormularioContacto(request.POST)
        if formulario_contacto.is_valid():
            # Recuperar los datos del formulario
            nombre = formulario_contacto.cleaned_data['nombre']
            correo = formulario_contacto.cleaned_data['correo']
            mensaje = formulario_contacto.cleaned_data['mensaje']
            send_mail(f'Mensaje de contacto de {nombre}',
                f'De: {nombre}\nCorreo: {correo}\n\n{mensaje}',
                correo,
                ['feliperin14@gmail.com'],
                fail_silently = True
                    )
            messages.success(request, 'Informacion enviada correctamente')
            return redirect('Contacto')
        else:
            messages.warning(request, 'la informacion no se envio correctamente intentalo nuevamente')
    else:
        formulario_contacto = FormularioContacto()
    
    return render(request,'contacto/contacto.html', {'formulario_contacto': formulario_contacto})
