from django.db import models
from accounts.models import User
from application.models import Asesorias

# Create your models here.



class HuellaDeCarbono(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcionsugerencias = models.ForeignKey('Retroalimentacion', on_delete=models.CASCADE)
    consumogasolina = models.FloatField()
    consumodiesel = models.FloatField()
    consumogasnaturalcomprimido = models.FloatField()
    consumogasnaturallicuado = models.FloatField()
    consumocarbonmineral = models.FloatField()
    consumocarbonvegetal = models.FloatField()
    ganadobovino = models.FloatField()
    ganadoovino = models.FloatField()
    ganadoporcino = models.FloatField()
    avicola = models.FloatField()
    consimoelectricidad = models.FloatField()
    generacionnorenovablehidraulica = models.FloatField()
    generacionnorenovablepetroloe = models.FloatField()
    generacionnorenovablenuclear = models.FloatField()
    consumopapel = models.FloatField()
    consumomovil = models.FloatField()
    consumocomputador = models.FloatField()
    consumoplastico = models.FloatField()
    consumotelevisor = models.FloatField()
    consumolavadora = models.FloatField()
    consumonevera = models.FloatField()

    cochemotocicleta = models.FloatField()
    cocheautmovilpequeño = models.FloatField()
    cocheautmovilmediano = models.FloatField()
    cocheautmovilgrande = models.FloatField()
    cocheautmovildeportivo = models.FloatField()
    cochesuvpequeño = models.FloatField()
    cochesuvmediano = models.FloatField()
    cochesuvgrande = models.FloatField()
    cochesuvdeportivo = models.FloatField()
    avion = models.FloatField()
    tren = models.FloatField()
    alimentacionres = models.FloatField()
    alimentacioncerdo = models.FloatField()
    alimentacionpollo = models.FloatField()
    alimentacionpescado = models.FloatField()


class Retroalimentacion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asesorias = models.ForeignKey(Asesorias, on_delete=models.CASCADE)
    huelladecarbonoR = models.ForeignKey(HuellaDeCarbono, on_delete=models.CASCADE)
    descripcionsugerencias = models.CharField(max_length=5000)
    cantidadsugerencias = models.PositiveSmallIntegerField(null=True)