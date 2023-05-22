from django.db import models
from accounts.models import User

class PQRSF(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pqrsf_entries")
    personalEncargado = models.ForeignKey('Asesorias', on_delete=models.CASCADE)
    fechaCreacion = models.DateField()
    fechaCierre = models.DateField()
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name="email_entries")
    numeroContacto = models.CharField(max_length=100)
    tipoPQRSF = models.CharField(max_length=100)
    detallesPQRSF = models.CharField(max_length=5000)
    evaluacionExperiencia = models.IntegerField()
    causaRaizPQRSF = models.CharField(max_length=5000)
    accionesCorrectivas = models.CharField(max_length=5000)

class Asesorias(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    numeroContacto = models.CharField(max_length=100)
    direcciondeContacto = models.CharField(max_length=100)
    personalEncargado = models.CharField(max_length=100)
    fechaSolicitud = models.DateField()
    fechaCierre = models.DateField()
    cantidadEmisionesGases = models.FloatField()
    objetivosMetasALlegar = models.CharField(max_length=5000)
    actividadesProcesosAImplementar = models.CharField(max_length=5000)
    presupuesto = models.FloatField()
    seguimientos = models.CharField(max_length=5000)























# from django.db import models
# from accounts.models import User
# from application.models import Asesorias
# from artificialIntelligence.models import Imagen
# from calculator.models import Retroalimentacion, HuellaDeCarbono
# # Create your models here.

# class PQRSF(models.Model):
#     username  = models.ForeignKey(User, on_delete=models.CASCADE)
#     personalEncargado = models.ForeignKey(Asesorias, on_delete=models.CASCADE)
#     fechaCreacion = models.DateField()
#     fechaCierre = models.DateField()
#     email = models.ForeignKey(User, on_delete=models.CASCADE)
#     numeroContacto = models.CharField(max_length=100)
#     tipoPQRSF = models.CharField(max_length=100)
#     detallesPQRSF = models.CharField(max_length=5000)
#     evaluacionExperiencia = models.IntegerField()
#     causaRaizPQRSF = models.CharField(max_length=5000)
#     accionesCorrectivas = models.CharField(max_length=5000)

# class Asesorias(models.Model):
#     username = models.ForeignKey(User, on_delete=models.CASCADE)
#     retroalimentacion = models.ForeignKey(Retroalimentacion, on_delete=models.CASCADE)
#     huelladecarbono = models.ForeignKey(HuellaDeCarbono, on_delete=models.CASCADE)
#     image = models.ForeignKey(Imagen, on_delete=models.CASCADE)
#     numeroContacto = models.CharField(max_length =100)
#     direcciondeContacto = models.CharField(max_length =100)
#     personalEncargado = models.CharField(max_length =100)
#     fechaSolicitud = models.DateField()
#     fechaCierre = models.DateField()
#     cantidadEmisionesGases = models.FloatField() ### REVISAR CON CALCULADORA
#     objetivosMetasALlegar = models.CharField(max_length =5000)
#     actividadesProcesosAImplementar = models.CharField(max_length =5000)
#     presupuesto = models.FloatField()
#     seguimientos = models.CharField(max_length =5000)