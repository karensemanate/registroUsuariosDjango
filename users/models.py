from django.db import models

# Create your models here.
class persona(models.model):
    
    ESTADO_CHOICES = [
        ('activo', 'activo'),
        ('inactivo','inactivo')
    ]
    name = models.CharField(max_length=20)
    cedula = models.CharField(max_length=100)
    telofono = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    estado = models.CharField(max_length=100, choices=ESTADO_CHOICES, default='activo')
    datacreate = models.DateFiel(auto_now=True)
