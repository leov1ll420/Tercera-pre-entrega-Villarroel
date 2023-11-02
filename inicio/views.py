from django.shortcuts import render, redirect
from inicio.models import Auto,Moto,Camion
from inicio.forms import CrearVehiculosFormulario

def inicio(request):
    
    return render(request,'inicio/inicio.html',{})

def vehiculos(request):
    marca_a_buscar=request.GET.get('marca')
    if marca_a_buscar:
        lista_de_autos= Auto.objects.filter(marca__icontains=marca_a_buscar)
    else:
        lista_de_autos= Auto.objects.all()

    
    return render(request, 'inicio/vehiculos.html',{'lista_de_autos':lista_de_autos})

def crear_vehiculos(request):

    if request.method== 'POST':
        formulario = CrearVehiculosFormulario(request.POST)
        if formulario.is_valid():
            info_limpia=formulario.cleaned_data
            
            marcaAuto=info_limpia.get('marcaAuto')
            descripcionAuto=info_limpia.get('descripcionAuto')
            añoAuto=info_limpia.get('añoAuto')
            
            marcaMoto=info_limpia.get('marcaMoto')
            descripcionMoto=info_limpia.get('descripcionMoto')
            añoMoto=info_limpia.get('añoMoto')
            
            marcaCamion=info_limpia.get('marcaCamion')
            descripcionCamion=info_limpia.get('descripcionCamion')
            añoCamion=info_limpia.get('añoCamion')
            
            auto=Auto(marca=marcaAuto.lower(), descripcion=descripcionAuto, año=añoAuto)
            auto.save()
            
            moto=Moto(marca=marcaMoto.lower(), descripcion=descripcionMoto, año=añoMoto)
            moto.save()
            
            camion=Camion(marca=marcaCamion.lower(), descripcion=descripcionCamion, año=añoCamion)
            camion.save()
            
            return redirect('vehiculos')
        else:
            return render(request, 'inicio/crear_vehiculos.html', {'formulario':formulario})
    formulario = CrearVehiculosFormulario()
    return render(request,'inicio/crear_vehiculos.html',{'formulario':formulario})

