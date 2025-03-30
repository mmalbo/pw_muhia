from django.urls import path
from .views import CrearSoicitudView

urlpatterns = [
    path('', CrearSoicitudView.as_view(template_name='servicio/solicitar.html'), name='solicitar_servicios'),
]