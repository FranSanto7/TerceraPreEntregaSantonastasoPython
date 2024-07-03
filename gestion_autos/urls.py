from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar_marca/', views.agregar_marca, name='agregar_marca'),
    path('agregar_modelo/', views.agregar_modelo, name='agregar_modelo'),
    path('buscar/', views.buscar, name='buscar'),
]