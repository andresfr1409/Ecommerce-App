from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True,max_length=100)
    correo = forms.EmailField(label='Correo electrónico', required=True)
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea)
