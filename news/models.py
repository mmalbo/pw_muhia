from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Curio(models.Model):
    title = models.CharField(max_length=200,verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = CKEditor5Field(default = "Texto", verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to="anuncion_evenet")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Curiosidad"
        verbose_name_plural = "Curiosidades"
        ordering = ['-created']

    def __str__(self):
        return self.title
    
    @property
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/img/bg-showcase-1.jpg"

class Event(models.Model):
    title = models.CharField(max_length=200,verbose_name="Título")
    description = CKEditor5Field(default = "Texto", verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="Contenido")
    start_time = models.DateTimeField(blank = False, null=True, verbose_name="Fecha del evento")
    end_time = models.DateTimeField(blank = False, null=True, verbose_name="Fecha del evento")
    created = models.DateTimeField(auto_now=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
    
    def __str__(self):
        return self.title