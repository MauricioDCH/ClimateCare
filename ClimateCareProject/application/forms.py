from django import forms

class PQTSFForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PQTSFForm, self).__init__(*args, **kwargs)
        self.fields['nombreUsuario'] =          forms.CharField(label='Nombre del usuario', required=True)
        self.fields['fechaCreacion'] =          forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker', 'placeholder': '03/12/2022'}), required=True, label='Fecha creación')
        self.fields['fechaCierre'] =            forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker', 'placeholder': '03/12/2022'}), required=True, label='Fecha cierre')
        self.fields['correoElectronico'] =      forms.EmailField(label='Correo electronico', required=True)
        self.fields['numeroContacto'] =         forms.CharField(label='Numero de contacto', required=True)
        self.fields['tipoPQRSF'] =              forms.CharField(label='Tipo de PQRSF', required=True)
        self.fields['detallesPQRSF'] =          forms.CharField(label='Detalles de la PQRSF', required=True)
        self.fields['evaluacionExperiencia'] =  forms.FloatField(label='Evaluacion de la experiencia', required=True)
        self.fields['causaRaizPQRSF'] =         forms.CharField(label='Causa raiz de la PQRSF', required=True)
        self.fields['accionesCorrectivas'] =    forms.CharField(label='Acciones correctivas', required=True)

class ASESORIASForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ASESORIASForm, self).__init__(*args, **kwargs)
        self.fields['nombreEntidad'] =                      forms.CharField(label='Nombre de la entidad', required=True)
        self.fields['numeroContacto'] =                     forms.CharField(label='Numero de contacto', required=True)
        self.fields['direcciondeContacto'] =                forms.CharField(label='Direccion de contacto', required=True)
        self.fields['personalEncargado'] =                  forms.CharField(label='Personal encargado', required=True)
        self.fields['fechaSolicitud'] =                     forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker', 'placeholder': '03/12/2022'}), required=True, label='Fecha solicitud')
        self.fields['fechaCierre'] =                        forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker', 'placeholder': '03/12/2022'}), required=True, label='Fecha cierre')
        self.fields['cantidadEmisionesGases'] =             forms.FloatField(label='Cantidad de emisiones de gases', required=True)
        self.fields['objetivosMetasALlegar'] =              forms.CharField(label='Objetivos y metas a llegar', required=True)
        self.fields['actividadesProcesosAImplementar'] =    forms.CharField(label='Actividades y procesos a implementar', required=True)
        self.fields['presupuesto'] =                        forms.FloatField(label='Presupuesto', required=True)
        self.fields['seguimientos'] =                       forms.CharField(label='Seguimientos', required=True)