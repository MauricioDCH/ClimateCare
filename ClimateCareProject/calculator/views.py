from django.shortcuts import render
from .forms import HuellaDeCarbonoForm
from django.contrib.auth.decorators import login_required
import random

@login_required
def calcular_huella(request):
    if request.method == 'POST':
        form = HuellaDeCarbonoForm(request.POST)
        if form.is_valid():
            # Inicializar variables

            consumoGasolina,consumoDiesel,consumoGasNaturalComprimido,consumoGasNaturalLicuado = 0,0,0,0
            consumoCarbonMineral,consumoCarbonVegetal,cantidadGanadoBovino,cantidadGanadoOvino,cantidadGanadoPorcino=0,0,0,0,0
            cantidadAvicola,consumoElectricidad,generacionElectricidadNoRenovableHidraulica=0,0,0
            generacionElectricidadNoRenovablePetroleo,generacionElectricidadNoRenovableNuclear,consumoPapel,consumoMoviles=0,0,0,0
            consumoPortatiles,consumoPlastico,consumoTV,consumoLavadora,consumoNevera=0,0,0,0,0
            
            consumoMotocicleta,consumoAutomovilMediano,consumoAutomovilGrande,consumoAutomovilDeportivo,= 0,0,0,0
            consumoSUVPequeno,consumoSUVMediano,consumoSUVGrande,consumoSUVDeportivo,consumoAutobus,consumoAvion,consumoBarco,consumoTren,consumoAgua,consumoRes= 0,0,0,0,0,0,0,0,0,0
            consumoCerdo,consumoPollo,consumoPescado = 0,0,0

            tablaHuella1 = {'consumoGasolina':{'entradaUsuario':consumoGasolina,'factorHuella':2.32,'unidades':'kgCO2e/L'},
                    'consumoDiesel':{'entradaUsuario':consumoDiesel,'factorHuella':2.67,'unidades':'kgCO2e/L'},
                    'consumoGasNaturalComprimido':{'entradaUsuario':consumoGasNaturalComprimido,'factorHuella':2.75,'unidades':'kgCO2e/L'},
                    'consumoGasNaturalLicuado':{'entradaUsuario':consumoGasNaturalLicuado,'factorHuella':1.79,'unidades':'kgCO2e/L'},
                    'consumoCarbonMineral':{'entradaUsuario':consumoCarbonMineral,'factorHuella':2.91,'unidades':'kgCO2e/Kg'},
                    'consumoCarbonVegetal':{'entradaUsuario':consumoCarbonVegetal,'factorHuella':3.67,'unidades':'kgCO2e/Kg'},
                    'cantidadGanadoBovino':{'entradaUsuario':cantidadGanadoBovino,'factorHuella':75.0,'unidades':'kgCO2e/cabeza/año'},
                    'cantidadGanadoOvino':{'entradaUsuario':cantidadGanadoOvino,'factorHuella':17.0,'unidades':'kgCO2e/cabeza/año'},
                    'cantidadGanadoPorcino':{'entradaUsuario':cantidadGanadoPorcino,'factorHuella':27.0,'unidades':'kgCO2e/cabeza/año'},
                    'cantidadAvicola':{'entradaUsuario':cantidadAvicola,'factorHuella':0.02,'unidades':'kgCO2e/cabeza/ciclo'},
                    'consumoElectricidad':{'entradaUsuario':consumoElectricidad,'factorHuella':0.475,'unidades':'kgCO2e/kWh'},
                    'generacionElectricidadNoRenovableHidraulica':{'entradaUsuario':generacionElectricidadNoRenovableHidraulica,'factorHuella':0.024,'unidades':'kgCO2e/kWh'},
                    'generacionElectricidadNoRenovablePetroleo':{'entradaUsuario':generacionElectricidadNoRenovablePetroleo,'factorHuella':0.51,'unidades':'kgCO2e/kWh'},
                    'generacionElectricidadNoRenovableNuclear':{'entradaUsuario':generacionElectricidadNoRenovableNuclear,'factorHuella':0.01,'unidades':'kgCO2e/kWh'},
                    'consumoPapel':{'entradaUsuario':consumoPapel,'factorHuella':0.83,'unidades':'kgCO2e/Kg'},'consumoMoviles':{'entradaUsuario':consumoMoviles,'factorHuella':60.0,'unidades':'kgCO2e/unidad'},
                    'consumoPortatiles':{'entradaUsuario':consumoPortatiles,'factorHuella':0.0,'unidades':'kgCO2e/unidad'},
                    'consumoPlastico':{'entradaUsuario':consumoPlastico,'factorHuella':6.0,'unidades':'kgCO2e/Kg'},
                    'consumoTV':{'entradaUsuario':consumoTV,'factorHuella':160.0,'unidades':'kgCO2e/unidades'},
                    'consumoLavadora':{'entradaUsuario':consumoLavadora,'factorHuella':220.0,'unidades':'kgCO2e/unidad'},
                    'consumoNevera':{'entradaUsuario':consumoNevera,'factorHuella':440.0,'unidades':'kgCO2e/unidad'},
                    'consumoMotocicleta':{'entradaUsuario':consumoMotocicleta,'factorHuella':0.12,'unidades':'kgCO2e/Km'},
                    'consumoAutomovilMediano':{'entradaUsuario':consumoAutomovilMediano,'factorHuella':0.20,'unidades':'kgCO2e/Km'},
                    'consumoAutomovilGrande':{'entradaUsuario':consumoAutomovilGrande,'factorHuella':0.24,'unidades':'kgCO2e/Km'},
                    'consumoAutomovilDeportivo':{'entradaUsuario':consumoAutomovilDeportivo,'factorHuella':0.25,'unidades':'kgCO2e/Km'},
                    'consumoSUVPequeno':{'entradaUsuario':consumoSUVPequeno,'factorHuella':0.20,'unidades':'kgCO2e/Km'},
                    'consumoSUVMediano':{'entradaUsuario':consumoSUVMediano,'factorHuella':0.24,'unidades':'kgCO2e/Km'},'consumoSUVGrande':
                    {'entradaUsuario':consumoSUVGrande,'factorHuella':0.28,'unidades':'kgCO2e/Km'},
                    'consumoSUVDeportivo':{'entradaUsuario':consumoSUVDeportivo,'factorHuella':0.35,'unidades':'kgCO2e/Km'},
                    'consumoAvion':{'entradaUsuario':consumoAvion,'factorHuella':0.25,'unidades':'kgCO2e/Km'},
                    'consumoTren':{'entradaUsuario':consumoTren,'factorHuella':0.04,'unidades':'kgCO2e/Km'},
                    'consumoRes':{'entradaUsuario':consumoRes,'factorHuella':27.0,'unidades':'kgCO2e/Kg'},
                    'consumoCerdo':{'entradaUsuario':consumoCerdo,'factorHuella':7.0,'unidades':'kgCO2e/Kg'},
                    'consumoPollo':{'entradaUsuario':consumoPollo,'factorHuella':6.5,'unidades':'kgCO2e/Kg'},
                    'consumoPescado':{'entradaUsuario':consumoPescado,'factorHuella':4.8,'unidades':'kgCO2e/Kg'}
                    }

            resultado = 0
            listaDatos = []
            for key, value in tablaHuella1.items():
                entradaUsuario = value['entradaUsuario']
                factorHuella = value['factorHuella']
                unidades = value['unidades']
                ingresos = form.cleaned_data[key]
                resultado += ingresos * factorHuella
            resultado =str(round(resultado, 2)) + ' kgCO2e'
            return render(request, 'resultCalculator.html',{'resultados': resultado}) 
    else:
        form = HuellaDeCarbonoForm()
    return render(request, 'formCalculator.html', {'form': form})


# @login_required
def recomendaciones(request):
    recomendaciones = {
        "Eficiencia energética en el hogar":
        [
            "Reduce el consumo de energía en el hogar",
            "Instala bombillas LED de bajo consumo.",
            "Utiliza electrodomésticos eficientes energéticamente"
            "Aprovecha la luz natural en lugar de encender luces durante el día.",
            "Ajusta la temperatura del termostato para reducir el uso de calefacción y aire acondicionado.",
            "Mejora el aislamiento de tu hogar.",
            "Utiliza el lavavajillas y la lavadora con carga completa.",
            "Desconecta los aparatos electrónicos cuando no los estés usando.",
        ],
        "Transporte sostenible":
        [
            "Conduce menos y utiliza el transporte público, camina o utiliza la bicicleta cuando sea posible.",
            "Comparte coche con otros para reducir el número de vehículos en la carretera.",
            "Elige vehículos con bajas emisiones de carbono, como los vehículos eléctricos.",
            "Mantén tu coche en buenas condiciones para que funcione de manera eficiente.",
            "Evita conducir a altas velocidades y acelerar y frenar bruscamente.",
            "Evita el uso de aviones para viajes cortos."
        ],
        "Reducción de desechos y reciclaje":
        [
            "Evita el uso de productos desechables y opta por alternativas reutilizables.",
            "Recicla tanto como sea posible.",
            "Reduce el consumo de papel.",
            "Utiliza bolsas reutilizables en lugar de bolsas de plástico desechables.",
            "Aprovecha el compostaje.",
            "Reduce el consumo de carne y lácteos.",
            "Compra alimentos locales y de temporada.",
            "Evita el desperdicio de alimentos."
        ],
            "Consumo consciente":
        [
                "Apoya a empresas y marcas sostenibles.",
                "Compra productos usados o de segunda mano.",
                "Evita el uso de productos químicos dañinos en el hogar y el jardín.",
                "Reduce el consumo de productos empaquetados en plástico.",
        ],
        "Conservación del agua:":
        [ 
            "Ahorra agua reduciendo el tiempo de ducha y recogiendo agua de lluvia.",
            "Arregla las fugas de agua y utiliza sistemas eficientes en tu hogar.",
            "Evita el uso de agua embotellada y utiliza un filtro de agua.",
            "Utiliza electrodomésticos eficientes energéticamente.",
            "Utiliza el lavavajillas y la lavadora con carga completa.",
            "No utilices el inodoro como papelera.",
            "No dejes el grifo abierto mientras te lavas los dientes o te afeitas."
        ],
        "Protección del medio ambiente":
        [
            "Planta árboles en tu comunidad.",
            "Apoya la conservación de la energía en el trabajo.",
            "Participa en programas de reforestación.",
            "Utiliza sistemas de captación de agua de lluvia.",
            "Promueve la educación y sensibilización ambiental en tu comunidad.",
            "Participa en programas de reciclaje.",
            "Participa en programas de limpieza de playas y ríos.",
            "Participa en programas de conservación de la biodiversidad.",
            "Participa en programas de conservación de los océanos.",
            "Participa en programas de conservación de los bosques.",
            "Participa en programas de conservación de los humedales."
        ],
        "Reducción de emisiones en el hogar": 
        [
            "Reduce el consumo de energía en el hogar.",
            "Apaga completamente los dispositivos electrónicos.",
            "Desconecta los cargadores de dispositivos electrónicos cuando no los uses.",
            "Utiliza sistemas de energía renovable en el hogar, como paneles solares.",
            "Utiliza electrodomésticos eficientes energéticamente.",
            "Aprovecha la luz natural en lugar de encender luces durante el día."
        ],
        "Estilo de vida sostenible": 
        [
            "Evita el uso excesivo de aire acondicionado y calefacción.",
            "Evita el uso de aerosoles.",
            "Reduce el consumo de agua embotellada.",
            "Minimiza el uso de aparatos de climatización y utiliza métodos naturales para mantener frescos o cálidos los espacios.",
            "Promueve el teletrabajo siempre que sea posible."
        ],
        "Gestión adecuada de residuos":
        [
            "Recupera y reutiliza el agua en el hogar.",
            "Participa en programas de intercambio y donación de ropa y otros artículos.",
            "Evita el despilfarro de alimentos.",
            "Utiliza papel reciclado y configura la impresora para imprimir a doble cara.",
            "Recicla y desecha correctamente los productos electrónicos y otros residuos peligrosos.",
            "Recicla y desecha correctamente los residuos orgánicos."
        ],
        "Promoción de prácticas sostenibles":
        [
            "Infórmate sobre el impacto ambiental de las empresas y marcas antes de realizar compras.",
            "Apoya iniciativas de conservación marina y evita el consumo de productos marinos en peligro de extinción o capturados de manera insostenible.",
            "Apoya la investigación y desarrollo de tecnologías limpias y sostenibles.",
            "Únete a grupos comunitarios y organizaciones medioambientales para trabajar en proyectos de acción climática y sensibilización."
        ],
        "Educación y concienciación":
        [
            "Educa a otros sobre la importancia de la reducción de la huella de carbono.",
            "Comparte información y recursos sobre prácticas sostenibles en tu comunidad.",
            "Participa en eventos y actividades relacionadas con el medio ambiente.",
            "Promueve la educación ambiental en escuelas y comunidades."
        ],
        "Energía renovable y eficiencia energética":[
            "Utiliza sistemas de energía renovable en el hogar, como paneles solares.",
            "Utiliza sistemas de energía solar pasiva.",
            "Utiliza sistemas de captación de agua de lluvia.",
            "Utiliza electrodomésticos eficientes energéticamente."
        ],
        "Movilización y acción colectiva": [
            "Únete a grupos de acción climática y sostenibilidad en tu comunidad.",
            "Participa en manifestaciones y actividades relacionadas con el cambio climático.",
            "Apoya políticas y medidas que promuevan una transición hacia una economía baja en carbono.",
            "Vota por líderes y políticas que respalden la sostenibilidad y la reducción de emisiones."
        ]
    }

    recomendaciones_totales = [recomendacion for lista in recomendaciones.values() for recomendacion in lista]
    if len(recomendaciones_totales) > 25:
        recomendaciones_totales = random.sample(recomendaciones_totales, 25)
    return render(request, 'recomendaciones.html', {'recomendaciones': recomendaciones_totales})





















# from pymongo import MongoClient
# from django.conf import settings

# client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
# db = client.get_database(settings.DATABASES['default']['NAME'])

# def index(request):
#     # client = MongoClient(settings.DATABASES['default']['CLIENT'])
#     # # db = client.get_database(settings.DATABASES['default']['NAME'])
#     # collection_names = db.list_collection_names()
#     # context = {'collection_names': collection_names}
#     # client.close() # Cierra la conexión con la base de datos
#     # return render(request, 'index.html', context)

#     # Obtener la colección "Categoria"
#     categoria_col = db["Categoria"]

#     # Crear un nuevo documento
#     nuevo_categoria = {
#         "nombre": "Categoria 5",
#         "descripcion": "Descripción de la categoría 5",
#         "estado": True,
#         "fecha_creacion": "2023-05-06"
#     }

#     # Insertar el nuevo documento en la colección
#     result = categoria_col.insert_one(nuevo_categoria)
#     print("El ID del nuevo documento es:", result.inserted_id)