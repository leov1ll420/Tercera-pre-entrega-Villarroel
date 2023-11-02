from django import forms 

class CrearVehiculosFormulario(forms.Form):
    marcaAuto= forms.CharField(max_length=30)
    descripcionAuto= forms.CharField(max_length=250)
    añoAuto=forms.IntegerField()
    
    marcaMoto= forms.CharField(max_length=30)
    descripcionMoto= forms.CharField(max_length=250)
    añoMoto=forms.IntegerField()
    
    marcaCamion= forms.CharField(max_length=30)
    descripcionCamion= forms.CharField(max_length=250)
    añoCamion=forms.IntegerField()