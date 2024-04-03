from django.contrib import admin
from .models import Pagina

class PageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pagina, PageAdmin)