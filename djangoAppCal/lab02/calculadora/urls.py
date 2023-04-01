from django.urls import path

from . import views

urlpatterns = [
    path('', views.formulario, name='formulario'),
    path('resultado', views.resultado, name='resultado'),
]
