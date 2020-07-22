from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic import DeleteView, DetailView, TemplateView

from django.contrib.auth.models import User
from django.http import HttpResponse
# from django.http import Http404
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from apps.proceso.forms import ProcesoForm
from apps.proceso.models import Proceso
from apps.decreto.models import Decreto
from apps.accion.models import Accion
from apps.citacion.models import Citacion
from apps.declaracion.models import Declaracion
from apps.declaraciontestigo.models import DeclaracionTestigo
from apps.acta.models import Acta
from apps.sentencia.models import Sentencia


def lista(request):
    listas = serializers.serialize('json', User.objects.all())
    return HttpResponse(listas, content_type='application/json')


class ProcesoList(LoginRequiredMixin, ListView):
    model = Proceso
    template_name = 'proceso/proceso_list.html'
    paginate_by = 20

    def get_queryset(self):
        object_list = Proceso.objects.all().order_by("-fecha")
        return object_list


class ProcesoCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'proceso.add_proceso'
    model = Proceso
    form_class = ProcesoForm
    template_name = 'proceso/proceso_form.html'
    success_message = "El proceso ha sido guardado manera exitosa."
    success_error = "El numero de radicado ya existe"

    def post(self, request, *args, **kwargs):
        try:
            if request.method == "POST":
                form = ProcesoForm(request.POST)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.save()
                    messages.success(self.request, self.success_message)
                return redirect('proceso:detalle', pk=post.pk)
        except UnboundLocalError:
            form = ProcesoForm()
            messages.success(self.request, self.success_error)
            return render(request, "proceso/proceso_form.html", {'form': form})


class ProcesoUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'proceso.change_proceso'
    model = Proceso
    form_class = ProcesoForm
    template_name = 'proceso/proceso_form.html'

    def get_success_url(self):
        procesoid = self.kwargs['pk']
        return reverse_lazy('proceso:detalle', kwargs={'pk': procesoid})


class ProcesoDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'proceso.delete_proceso'
    model = Proceso
    template_name = 'proceso/proceso_delete.html'
    success_url = reverse_lazy('proceso:listado')
    success_message = "ha sido eliminado exitosamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ProcesoDelete, self).delete(request, *args, **kwargs)


class BuscarView(LoginRequiredMixin, ListView):
    model = Proceso
    template_name = 'proceso/proceso_list.html'
    success_error = "consulta inexistentes"

    def post(self, request):
        try:
            buscar = request.POST['buscalo']
            if buscar != '':
                object_list = Proceso.objects.filter(
                    radicado__contains=buscar) | Proceso.objects.filter(
                        expediente=buscar) | Proceso.objects.filter(
                            nombre__contains=buscar) | Proceso.objects.filter(
                                tipo__nombre=buscar) | Proceso.objects.filter(
                                    diocesis__nombre=buscar)
            else:
                object_list = Proceso.objects.all()
            return render(request, "proceso/proceso_list.html", {'object_list': object_list})
        except Proceso.DoesNotExist:
            object_list = Proceso.objects.all()
            messages.success(self.request, self.success_message)
            return render(request, "proceso/proceso_list.html", {'object_list': object_list})
        except ValueError:
            object_list = Proceso.objects.all()
            messages.success(self.request, self.success_error)
            return render(request, "proceso/proceso_list.html", {'object_list': object_list})


class DetalleList(LoginRequiredMixin, DetailView):
    model = Proceso
    template_name = 'proceso/proceso.html'


class Actividad(LoginRequiredMixin, TemplateView):
    model = Accion, Decreto, Declaracion, Citacion, Acta, Sentencia, DeclaracionTestigo
    template_name = 'proceso/actividad.html'

    def get(self, request, *args, **kwargs):
        object_list1 = Accion.objects.filter(
            proceso_id=self.kwargs['pk']).values('nombre__tipo', 'fecha')
        object_list2 = Decreto.objects.filter(
            proceso_id=self.kwargs['pk']).values('nombre__tipo', 'fecha')
        object_list3 = Citacion.objects.filter(
            proceso_id=self.kwargs['pk']).values('nombre__tipo', 'fecha')
        object_list4 = Declaracion.objects.filter(
            proceso_id=self.kwargs['pk']).values('nombre__tipo', 'fecha')
        object_list5 = Acta.objects.filter(
            proceso_id=self.kwargs['pk']).values('nombre', 'fecha')
        object_list6 = Sentencia.objects.filter(
            proceso_id=self.kwargs['pk']).values('nombre', 'fecha')
        object_list7 = DeclaracionTestigo.objects.filter(
            proceso_id=self.kwargs['pk']).values('nombre__tipo', 'fecha')
        result_list = object_list1.union(object_list2, all=True).union(
            object_list3, all=True).union(object_list4, all=True).union(
                object_list5, all=True).union(object_list6, all=True).union(
                    object_list7, all=True).order_by('fecha')
        procesodata = Proceso.objects.get(radicado=self.kwargs['pk'])
        return render(request, 'proceso/actividad.html',
                      {'result_list': result_list, 'procesodata': procesodata})


class Consulta(TemplateView):
    model = Proceso
    template_name = 'proceso/consulta.html'
    success_message = "El Proceso No Esta Registrado."

    def post(self, request):
        try:
            buscar = request.POST['buscalo']
            if buscar != '':
                object_list1 = Accion.objects.filter(
                    proceso__radicado=buscar).values('nombre__tipo', 'fecha')
                object_list2 = Decreto.objects.filter(
                    proceso__radicado=buscar).values('nombre__tipo', 'fecha')
                object_list3 = Citacion.objects.filter(
                    proceso__radicado=buscar).values('nombre__tipo', 'fecha')
                object_list4 = Declaracion.objects.filter(
                    proceso__radicado=buscar).values('nombre__tipo', 'fecha')
                object_list5 = Acta.objects.filter(
                    proceso__radicado=buscar).values('nombre', 'fecha')
                object_list6 = Sentencia.objects.filter(
                    proceso__radicado=buscar).values('nombre', 'fecha')
                object_list7 = DeclaracionTestigo.objects.filter(
                    proceso__radicado=buscar).values('nombre__tipo', 'fecha')
                result_list = object_list1.union(object_list2, all=True).union(
                    object_list3, all=True).union(object_list4, all=True).union(
                        object_list5, all=True).union(object_list6, all=True).union(
                            object_list7, all=True).order_by('fecha')
                procesodata = Proceso.objects.get(radicado=buscar)
            else:
                result_list = Proceso.objects.get(radicado=buscar)
            return render(request, "proceso/consulta.html",
                          {'result_list': result_list, 'procesodata': procesodata})
        except Proceso.DoesNotExist:
            messages.success(self.request, self.success_message)
            return render(request, "proceso/consulta.html")
        except ValueError:
            messages.success(self.request, self.success_message)
            return render(request, "proceso/consulta.html")
