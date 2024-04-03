from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Pagina(models.Model):
    title = models.CharField(null = False, blank = False, max_length=200, verbose_name="Título")
    content = CKEditor5Field(default = "Texto", verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['title']

    def __str__(self):
        return self.title