from django.urls import path
from . import views

urlpatterns = [
    path('curiosidades/', views.curios, name="curios"),
    path('calendario/', views.CalendarView.as_view(), name='calendar'),
]