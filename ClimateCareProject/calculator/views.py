from django.shortcuts import render
from .forms import HuellaDeCarbonoForm
from django.contrib.auth.decorators import login_required

@login_required
def calcular_huella(request):
    if request.method == 'POST':
        form = HuellaDeCarbonoForm(request.POST)
        if form.is_valid():
            # Inicializar variables

            tablaHuella1,idUsuario,idRetroalimentacion,idImagen,idCompania,consumoGasolina,consumoDiesel,consumoGasNaturalComprimido,consumoGasNaturalLicuado = 0,0,0,0,0,0,0,0,0
            consumoCarbonMineral,consumoCarbonVegetal,consumoLenia,cantidadGanadoBovino,cantidadGanadoOvino,cantidadGanadoPorcino,cantidadGanadoCaprino=0,0,0,0,0,0,0
            cantidadAvicola,consumoElectricidad,generacionElectricidadRenovable,generacionElectricidadNoRenovableCarbon,generacionElectricidadNoRenovableHidraulica=0,0,0,0,0
            generacionElectricidadNoRenovableGasNatural,generacionElectricidadNoRenovablePetroleo,generacionElectricidadNoRenovableNuclear,consumoPapel,consumoMoviles=0,0,0,0,0
            consumoPortatiles,consumoCemento,consumoVidrio,consumoPlastico,consumoAluminio,consumoTV,consumoLavadora,consumoNevera,consumoMicroondas,consumoOtrosElectronicos=0,0,0,0,0,0,0,0,0,0
            
            tablaHuella2,consumoMotocicleta,consumoAutomovilPequeno,consumoAutomovilMediano,consumoAutomovilGrande,consumoAutomovilDeportivo,= 0,0,0,0,0,0
            consumoSUVPequeno,consumoSUVMediano,consumoSUVGrande,consumoSUVDeportivo,consumoAutobus,consumoAvion,consumoBarco,consumoTren,consumoAgua,consumoRes= 0,0,0,0,0,0,0,0,0,0
            consumoCerdo,consumoPollo,consumoPescado,consumoFrutasYVerduras,consumoHuevos,consumoLeche,consumoQueso,consumoCacao,consumoCafe,consumoAzucar,consumoCereal = 0,0,0,0,0,0,0,0,0,0,0
            consumoAceite,consumoBebidasAlcoholicas =0,0

            tablaHuella1 = {'tablaHuella1':{'entradaUsuario':tablaHuella1,'factorHuella':0,'unidades':""},'idUsuario':  {'entradaUsuario':idUsuario,'factorHuella':0,'unidades':""},
                    'idRetroalimentacion':{'entradaUsuario':idRetroalimentacion,'factorHuella':0,'unidades':""},'idImagen':{'entradaUsuario':idImagen,'factorHuella':0,'unidades':""},
                    'idCompania':{'entradaUsuario':idCompania,'factorHuella':0,'unidades':""},'consumoGasolina':{'entradaUsuario':consumoGasolina,'factorHuella':2.32,'unidades':'kgCO2e/L'},
                    'consumoDiesel':{'entradaUsuario':consumoDiesel,'factorHuella':2.67,'unidades':'kgCO2e/L'},'consumoGasNaturalComprimido':{'entradaUsuario':consumoGasNaturalComprimido,'factorHuella':2.75,'unidades':'kgCO2e/L'},
                    'consumoGasNaturalLicuado':{'entradaUsuario':consumoGasNaturalLicuado,'factorHuella':1.79,'unidades':'kgCO2e/L'},'consumoCarbonMineral':{'entradaUsuario':consumoCarbonMineral,'factorHuella':2.91,'unidades':'kgCO2e/Kg'},
                    'consumoCarbonVegetal':{'entradaUsuario':consumoCarbonVegetal,'factorHuella':3.67,'unidades':'kgCO2e/Kg'},'consumoLenia':{'entradaUsuario':consumoLenia,'factorHuella':1.98,'unidades':'kgCO2e/Kg'},
                    'cantidadGanadoBovino':{'entradaUsuario':cantidadGanadoBovino,'factorHuella':75.0,'unidades':'kgCO2e/cabeza/ano'},'cantidadGanadoOvino':{'entradaUsuario':cantidadGanadoOvino,'factorHuella':17.0,'unidades':'kgCO2e/cabeza/ano'},
                    'cantidadGanadoPorcino':{'entradaUsuario':cantidadGanadoPorcino,'factorHuella':27.0,'unidades':'kgCO2e/cabeza/ano'},'cantidadGanadoCaprino':{'entradaUsuario':cantidadGanadoCaprino,'factorHuella':1.5,'unidades':'kgCO2e/cabeza/ano'},
                    'cantidadAvicola':{'entradaUsuario':cantidadAvicola,'factorHuella':0.02,'unidades':'kgCO2e/cabeza/ciclo'},'consumoElectricidad':{'entradaUsuario':consumoElectricidad,'factorHuella':0.475,'unidades':'kgCO2e/kWh'},
                    'generacionElectricidadRenovable':{'entradaUsuario':generacionElectricidadRenovable,'factorHuella':0.0,'unidades':'kgCO2e/kWh'},
                    'generacionElectricidadNoRenovableCarbon':{'entradaUsuario':generacionElectricidadNoRenovableCarbon,'factorHuella':0.82,'unidades':'kgCO2e/kWh'},
                    'generacionElectricidadNoRenovableHidraulica':{'entradaUsuario':generacionElectricidadNoRenovableHidraulica,'factorHuella':0.024,'unidades':'kgCO2e/kWh'},
                    'generacionElectricidadNoRenovableGasNatural':{'entradaUsuario':generacionElectricidadNoRenovableGasNatural,'factorHuella':0.18,'unidades':'kgCO2e/kWh'},
                    'generacionElectricidadNoRenovablePetroleo':{'entradaUsuario':generacionElectricidadNoRenovablePetroleo,'factorHuella':0.51,'unidades':'kgCO2e/kWh'},
                    'generacionElectricidadNoRenovableNuclear':{'entradaUsuario':generacionElectricidadNoRenovableNuclear,'factorHuella':0.01,'unidades':'kgCO2e/kWh'},
                    'consumoPapel':{'entradaUsuario':consumoPapel,'factorHuella':0.83,'unidades':'kgCO2e/Kg'},'consumoMoviles':{'entradaUsuario':consumoMoviles,'factorHuella':60.0,'unidades':'kgCO2e/unidad'},
                    'consumoPortatiles':{'entradaUsuario':consumoPortatiles,'factorHuella':0.0,'unidades':'kgCO2e/unidad'},'consumoCemento':{'entradaUsuario':consumoCemento,'factorHuella':0.58,'unidades':'kgCO2e/Kg'},
                    'consumoVidrio':{'entradaUsuario':consumoVidrio,'factorHuella':0.57,'unidades':'kgCO2e/Kg'},'consumoPlastico':{'entradaUsuario':consumoPlastico,'factorHuella':6.0,'unidades':'kgCO2e/Kg'},
                    'consumoAluminio':{'entradaUsuario':consumoAluminio,'factorHuella':11.0,'unidades':'kgCO2e/Kg'},'consumoTV':{'entradaUsuario':consumoTV,'factorHuella':160.0,'unidades':'kgCO2e/unidades'},
                    'consumoLavadora':{'entradaUsuario':consumoLavadora,'factorHuella':220.0,'unidades':'kgCO2e/unidad'},'consumoNevera':{'entradaUsuario':consumoNevera,'factorHuella':440.0,'unidades':'kgCO2e/unidad'},
                    'consumoMicroondas':{'entradaUsuario':consumoMicroondas,'factorHuella':100.0,'unidades':'kgCO2e/unidad'},'consumoOtrosElectronicos':{'entradaUsuario':consumoOtrosElectronicos,'factorHuella':125,'unidades':'kgCO2e/unidad'},
                            # }
            ## Tabla Huella 2
            # tablaHuella2={
                    'tablaHuella1':{'entradaUsuario':tablaHuella1,'factorHuella':0,'unidades':""},'tablaHuella2':{'entradaUsuario':tablaHuella1,'factorHuella':0,'unidades':""},
                    'consumoMotocicleta':{'entradaUsuario':consumoMotocicleta,'factorHuella':0.12,'unidades':'kgCO2e/Km'},'consumoAutomovilPequeno':{'entradaUsuario':consumoAutomovilPequeno,'factorHuella':0.16,'unidades':'kgCO2e/Km'},
                    'consumoAutomovilMediano':{'entradaUsuario':consumoAutomovilMediano,'factorHuella':0.20,'unidades':'kgCO2e/Km'},'consumoAutomovilGrande':{'entradaUsuario':consumoAutomovilGrande,'factorHuella':0.24,'unidades':'kgCO2e/Km'},
                    'consumoAutomovilDeportivo':{'entradaUsuario':consumoAutomovilDeportivo,'factorHuella':0.25,'unidades':'kgCO2e/Km'},'consumoSUVPequeno':{'entradaUsuario':consumoSUVPequeno,'factorHuella':0.20,'unidades':'kgCO2e/Km'},
                    'consumoSUVMediano':{'entradaUsuario':consumoSUVMediano,'factorHuella':0.24,'unidades':'kgCO2e/Km'},'consumoSUVGrande':{'entradaUsuario':consumoSUVGrande,'factorHuella':0.28,'unidades':'kgCO2e/Km'},
                    'consumoSUVDeportivo':{'entradaUsuario':consumoSUVDeportivo,'factorHuella':0.35,'unidades':'kgCO2e/Km'},'consumoAutobus':{'entradaUsuario':consumoAutobus,'factorHuella':0.07,'unidades':'kgCO2e/Km'},
                    'consumoAvion':{'entradaUsuario':consumoAvion,'factorHuella':0.25,'unidades':'kgCO2e/Km'},'consumoBarco':{'entradaUsuario':consumoBarco,'factorHuella':0.08,'unidades':'kgCO2e/pKm'},
                    'consumoTren':{'entradaUsuario':consumoTren,'factorHuella':0.04,'unidades':'kgCO2e/Km'},'consumoAgua':{'entradaUsuario':consumoAgua,'factorHuella':0.00005,'unidades':'kgCO2e/L'},
                    'consumoRes':{'entradaUsuario':consumoRes,'factorHuella':27.0,'unidades':'kgCO2e/Kg'},'consumoCerdo':{'entradaUsuario':consumoCerdo,'factorHuella':7.0,'unidades':'kgCO2e/Kg'},
                    'consumoPollo':{'entradaUsuario':consumoPollo,'factorHuella':6.5,'unidades':'kgCO2e/Kg'},'consumoPescado':{'entradaUsuario':consumoPescado,'factorHuella':4.8,'unidades':'kgCO2e/Kg'},
                    'consumoFrutasYVerduras':{'entradaUsuario':consumoFrutasYVerduras,'factorHuella':0.4,'unidades':'kgCO2e/Kg'},'consumoHuevos':{'entradaUsuario':consumoHuevos,'factorHuella':2.7,'unidades':'kgCO2e/Kg'},
                    'consumoLeche':{'entradaUsuario':consumoLeche,'factorHuella':1.9,'unidades':'kgCO2e/L'},'consumoQueso':{'entradaUsuario':consumoQueso,'factorHuella':13.5,'unidades':'kgCO2e/Kg'},
                    'consumoCacao':{'entradaUsuario':consumoCacao,'factorHuella':4.4,'unidades':'kgCO2e/Kg'},'consumoCafe':{'entradaUsuario':consumoCafe,'factorHuella':17.0,'unidades':'kgCO2e/Kg'},
                    'consumoAzucar':{'entradaUsuario':consumoAzucar,'factorHuella':1.1,'unidades':'kgCO2e/Kg'},'consumoCereal':{'entradaUsuario':consumoCereal,'factorHuella':1.3,'unidades':'kgCO2e/Kg'},
                    'consumoAceite':{'entradaUsuario':consumoAceite,'factorHuella':2.3,'unidades':'kgCO2e/Kg'},'consumoBebidasAlcoholicas':{'entradaUsuario':consumoBebidasAlcoholicas,'factorHuella':3.9,'unidades':'kgCO2e/L'}}

            resultado = 0
            listaDatos = []
            for key, value in tablaHuella1.items():
                entradaUsuario = value['entradaUsuario']
                factorHuella = value['factorHuella']
                unidades = value['unidades']
                ingresos = form.cleaned_data[key]
                resultado += ingresos * factorHuella
                datos = key + " || " + str(ingresos) + " || " + str(factorHuella) + " || " + str(ingresos*factorHuella) + " || " + unidades
                listaDatos.append(datos)
            resultado =str(round(resultado, 2)) + ' kgCO2e'
            return render(request, 'resultCalculator.html',{'datos':listaDatos ,'resultados': resultado})#, 'form1':variables, 'form2':factoresHuella,'form3':total,'datos': datos}) 
    else:
        form = HuellaDeCarbonoForm()
    return render(request, 'formCalculator.html', {'form': form})

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