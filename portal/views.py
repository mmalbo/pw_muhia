from calendar import HTMLCalendar, Calendar
from pkgutil import get_data
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from pages.models import Pagina 
from galeria.models import banner, imagenes
from enlac_preg.models import Pregunta, Enlaces
from news.models import Curio
from django.utils.safestring import mark_safe

from .models import *
from news.utils import Calendar, get_date

#from galeria import imagenes,banner
#from proyectos_muhia.galeria.models import banner
# Create your views here.

def inicio(request):
    g_imagenes = imagenes.objects.all()
    #banner.activo==True
    banner1 = banner.objects.get(id=1)
    sitios = Enlaces.objects.all()
    curios_count = Curio.objects.count()
    curios1 = Curio.objects.get(pk=curios_count)
    curios2 = Curio.objects.get(pk=curios_count-1)
    """ Calendario """
    # use today's date for the calendar
    d = get_date(request.GET.get('day', None))

    # Instantiate our calendar class with today's year and date
    cal = Calendar(d.year, d.month)

    # Call the formatmonth method, which returns our calendar as a table
    html_cal = cal.formatmonth(withyear=True)
    return render(request, "index.html", locals())

def nosotros(request):
    return render(request, "About/nosotros.html", {})

def historia(request):
    return render(request, "About/historia.html", {})

def equipo(request):
    return render(request, "About/equipo.html", {})

def productos(request):
    g_imagenes = imagenes.objects.all()
    img1 = imagenes.objects.get(pk=1)
    return render(request, "products.html", locals())

def servicios(request):
    return render(request, "service.html", {})

def preguntas(request):
    Preg = Pregunta.objects.all()
    return render(request, "preg_frec.html", locals())

def contacto(request):
    return render(request, "contacto.html", {})
#return HttpResponse("Hola mundo. Al fin tenemos una aplicacion visible.")
