from django.db import models

# Create your models here.
class imagenes(models.Model):
    title = models.CharField(null = False, blank = False, max_length = 200, verbose_name = "Nombre")
    image = models.ImageField(null = False, upload_to = "galeria", verbose_name= "Imagen")  
    activo = models.BooleanField(null = False, default = True)
    is_product = models.BooleanField(null=True, blank= True, verbose_name="Para la sección productos")
    created = models.DateTimeField(auto_now = True, verbose_name = "Fecha de creación")

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imágenes"
        ordering = ['created']

    def _str_(self):
        return self.title
    
    @property
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/img/carousel/carousel.jpeg"
            
    
class banner(models.Model):
    title = models.CharField(null = False, blank = False, max_length = 200, verbose_name = "Nombre")
    image = models.ImageField(null = False, upload_to = "banners", verbose_name= "Imagen")
    activo = models.BooleanField(null = False, default = True)
    created = models.DateTimeField(auto_now = True, verbose_name = "Fecha de creación")

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"
        ordering = ['created']

    def _str_(self):
        return self.title
    
    @property
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/img/carousel/carousel.jpeg"
