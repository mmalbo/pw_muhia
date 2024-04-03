#from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('quien/', views.nosotros, name="quienes"),
    path('historia/', views.historia, name="historia"),
    path('equipo/', views.equipo, name="equipo"),
    path('productos/', views.productos, name="productos"),
    path('servicios/', views.servicios, name="servicios"),
    path('preguntas/', views.preguntas, name="preguntas"),
    path('contacto/', views.contacto, name="contacto"),
    path('news/', include('news.urls')),
    path('accounts', include('django.contrib.auth.urls')),
    path('accounts', include('registration.urls')),
#    path()
]

