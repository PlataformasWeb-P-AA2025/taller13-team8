from django.db import models

# Create your models here.

class Edificio(models.Model):
    
    CHOICES = [
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial'),
    ]

    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices= CHOICES)

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - {self.ciudad}"


class Departamento(models.Model):
    nombre_propietario = models.CharField(max_length=150)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    numero_cuartos = models.IntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE, related_name='departamentos')

    def __str__(self):
        return f"{self.nombre_propietario} - {self.edificio.nombre}"