from django.contrib import admin
from inicio.models import Auto,Moto,Camion

admin.site.register(Auto, Moto, Camion)