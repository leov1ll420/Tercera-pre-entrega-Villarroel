from django.db import models

class Auto(models.Model):
    marca= models.CharField( max_length=30)
    descripcion = models.TextField()
    año= models.IntegerField()
    
    def __str__(self):
        return f'{self.id}-{self.marca}-{self.año}'

class Moto(models.Model):
    marca= models.CharField( max_length=30)
    descripcion = models.TextField()
    año= models.IntegerField()
    
    def __str__(self):
        return f'{self.id}-{self.marca}-{self.año}'
    
class Camion(models.Model):
    marca= models.CharField( max_length=30)
    descripcion = models.TextField()
    año= models.IntegerField()
    
    def __str__(self):
        return f'{self.id}-{self.marca}-{self.año}'
