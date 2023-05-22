from django.shortcuts import render
from .forms import PQTSFForm, ASESORIASForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def PQRSF(request):
    if request.method == 'POST':
        form = PQTSFForm(request.POST)
        if form.is_valid():
            # Inicializar variables
            nombreUsuario, fechaCreacion, fechaCierre,correoElectronico,numeroContacto, tipoPQRSF, detallesPQRSF,evaluacionExperiencia,causaRaizPQRSF,accionesCorrectivas= "", "", "", "", "", "", "", 0, "", ""
            listaNombresPQRSF = ['nombreUsuario', 'fechaCreacion', 'fechaCierre', 'correoElectronico', 'numeroContacto', 'tipoPQRSF', 'detallesPQRSF', 'evaluacionExperiencia', 'causaRaizPQRSF', 'accionesCorrectivas']
            listaPQRSF =[]
            for data in listaNombresPQRSF:
                if data in form.cleaned_data:
                    ingresos = form.cleaned_data[data]
                    listaPQRSF.append(ingresos)
            return render(request, 'resultadoPQRSF.html',{'resultados': listaPQRSF}) 
    else:
        form = PQTSFForm()
    return render(request, 'formPQRSF.html', {'form': form})

@login_required
def ASERORIAS(request):
    if request.method == 'POST':
        form = ASESORIASForm(request.POST)
        if form.is_valid():
            # Inicializar variables
            nombreEntidad, numeroContacto, direcciondeContacto, personalEncargado, fechaSolicitud, fechaCierre, cantidadEmisionesGases, objetivosMetasALlegar, actividadesProcesosAImplementar, presupuesto, seguimiento = "","" ,"", "", "", "", 0, "", "", 0, ""
            listaNombresAsesoria = ['nombreEntidad', 'numeroContacto', 'direcciondeContacto', 'personalEncargado', 'fechaSolicitud', 'fechaCierre', 'cantidadEmisionesGases', 'objetivosMetasALlegar', 'actividadesProcesosAImplementar', 'presupuesto', 'seguimiento']
            listaAsesoria =[]
            for data in listaNombresAsesoria:
                if data in form.cleaned_data:
                    ingresos = form.cleaned_data[data]
                    listaAsesoria.append(ingresos)
            return render(request, 'resultadoAsesoria.html',{'resultados': listaAsesoria})
    else:
        form = ASESORIASForm()
    return render(request, 'formAsesoria.html', {'form': form})
