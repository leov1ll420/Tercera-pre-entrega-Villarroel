from django.urls import path
from inicio.views import inicio, crear_vehiculos, vehiculos


urlpatterns = [
    path('',inicio, name='inicio'),
    path('vehiculos/',vehiculos, name='vehiculos'),
    path('vehiculos/crear', crear_vehiculos,name='crear_vehiculos')
]