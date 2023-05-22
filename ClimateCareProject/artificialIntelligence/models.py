from django.db import models
from accounts.models import User
from calculator.models import Retroalimentacion, HuellaDeCarbono

class matchingLearningModels(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    architecture = models.FileField(upload_to='matchingLearningModels/')
    weights = models.FileField(upload_to='matchingLearningModels/')
    priority = models.PositiveSmallIntegerField(null=True)

class Imagen(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey('CategoriaImagenes', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    porcentajeCerteza = models.FloatField(null=True)

class CategoriaImagenes(models.Model):
    title = models.CharField(max_length=50)
    numberOfImages = models.PositiveSmallIntegerField(null=True)

class Companias(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    retroalimentacion = models.ForeignKey(Retroalimentacion, on_delete=models.CASCADE, default=0)
    huelladecarbono = models.ForeignKey(HuellaDeCarbono, on_delete=models.CASCADE, default=0)
    metodosprocesos = models.ForeignKey('MetodosProcesos', on_delete=models.CASCADE, default=0)
    nombrecompania = models.CharField(max_length=50)
    direccioncompania = models.CharField(max_length=200)
    materialesquereciclan = models.CharField(max_length=200)
    cantidadmaterialesreciclados = models.FloatField()
    certificados = models.CharField(max_length=2000)
    tarifas = models.FloatField()

class MetodosProcesos(models.Model):
    compania = models.ForeignKey(User, on_delete=models.CASCADE, related_name="compania_entries")
    nombreproceso = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=2000)


