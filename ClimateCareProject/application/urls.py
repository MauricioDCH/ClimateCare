from django.urls import path
from . import views as applicationViews

urlpatterns = [
    path('', applicationViews.PQRSF, name='pqrsf'),
    path('asesoria/', applicationViews.ASERORIAS, name='asesorias'),
]