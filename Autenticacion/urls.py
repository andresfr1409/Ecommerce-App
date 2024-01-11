from django.urls import path
from Autenticacion import views 

urlpatterns = [
    path('registro/', views.registro, name='registro'),
]
