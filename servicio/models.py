from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
    
class Solicitud(models.Model):
    usuario = models.CharField(max_length=100, verbose_name='Nombre y apellidos')
    telefono = models.CharField(max_length=10, null='True', verbose_name='Teléfono (Con WhatsApp)')
    correo = models.CharField(max_length=10, null='True', verbose_name='Correo electrónico')
    carnet = models.CharField(max_length=11)
    servicios = models.ManyToManyField(Servicio)
    fecha_solicitud = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Solicitud de {self.usuario}"