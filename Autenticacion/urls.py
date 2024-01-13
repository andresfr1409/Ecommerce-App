from django.urls import path
from Autenticacion import views 

urlpatterns = [
    path('registro/', views.Vregistro.as_view(), name='registro'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion')
]
