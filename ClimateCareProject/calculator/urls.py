from django.contrib import admin
from django.urls import path
from . import views as calculatorViews

urlpatterns = [
    path('', calculatorViews.calcular_huella, name = 'calculator'),
    path('recomendaciones/', calculatorViews.recomendaciones, name = 'recomendaciones'),
]
