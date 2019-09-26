from django.shortcuts import render
from django.views.generic.base import TemplateView

# importamos los movimientos
from movimientos.models import Asignacion, Material_Asignado
from .models import Perfil
from easy_pdf.views import PDFTemplateView
# Importamos la libreria de tiempo
import datetime
# Create your views here.


class T_Responsabilidad_PDF(PDFTemplateView, TemplateView):
    template_name = 'T_Responsabilidad.html'

    def get_context_data(self, **kwargs):
        ids = self.request.GET.get('id')
        algo = []
        perfil = Perfil.objects.filter(id=ids).get()
        now = datetime.datetime.now()
        try:
            asig = Asignacion.objects.filter(assigned_to=ids)
            for asig in asig:
                for mater in Material_Asignado.objects.filter(
                        id_asignacion=asig.id_no):
                    algo.append(mater)
            for asignacion in Asignacion.objects.filter(assigned_to=ids):
                asignacion
            today = datetime.date.today
            numero = Asignacion.objects.filter(
                assigned_to=ids).count()
            numero_acep = Asignacion.objects.filter(
                assigned_to=ids, estado=True).count()
            numero_pendi = Asignacion.objects.filter(
                assigned_to=ids, estado=False).count()

            return super(T_Responsabilidad_PDF, self).get_context_data(
                pagesize='Legal landscape',
                title='Tarjeta de Responsabilidad',
                algo=algo,
                asignacion=asignacion,
                numero=numero,
                now=now,
                aceptadas=numero_acep,
                pendientes=numero_pendi,
                today=today,
                perfil=perfil,
                **kwargs
                )
        except:
            numero = 0
            numero_pendi = 0
            return super(T_Responsabilidad_PDF, self).get_context_data(
                pagesize='Legal landscape',
                title='Tarjeta de Responsabilidad',
                today=today,
                now=now,
                perfil=perfil,
                numero=numero,
                pendientes=numero_pendi,
                **kwargs
                )
