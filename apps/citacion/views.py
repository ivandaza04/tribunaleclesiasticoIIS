from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from apps.citacion.forms import CitacionForm
from apps.citacion.models import Citacion


def lista(request):
    listas = serializers.serialize('json', User.objects.all())
    return HttpResponse(listas, content_type='application/json')


class CitacionList(LoginRequiredMixin, ListView):
    model = Citacion
    template_name = 'citacion/citacion_list.html'

    def get_queryset(self):
        object_list = Citacion.objects.filter(
            proceso_id=self.kwargs['pk'])
        return object_list


class CitacionCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'citacion.add_citacion'
    model = Citacion
    form_class = CitacionForm
    template_name = 'citacion/citacion_form.html'

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = CitacionForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.proceso_id = self.kwargs['fk']
                post.save()
            return redirect('citacion:detalle', pk=post.pk)
        else:
            form = CitacionForm()
        return render('citacion/citacion_form.html', {'form': form})


class CitacionUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'citacion.change_citacion'
    model = Citacion
    form_class = CitacionForm
    template_name = 'citacion/citacion_form.html'

    def get_success_url(self):
        value = self.kwargs['pk']
        return reverse_lazy('citacion:detalle', kwargs={'pk': value})


class CitacionDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'citacion.delete_citacion'
    model = Citacion
    template_name = 'citacion/citacion_delete.html'
    success_url = reverse_lazy('proceso:listado')
    success_message = "ha sido eliminado exitosamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(CitacionDelete, self).delete(request, *args, **kwargs)


class BuscarView(LoginRequiredMixin, ListView):
    model = Citacion
    template_name = 'citacion/citacion_list.html'

    def post(self, request):
        try:
            buscar = request.POST['buscalo']
            if buscar != '':
                object_list = Citacion.objects.filter(
                    proceso__expediente=buscar) | Citacion.objects.filter(proceso__nombre=buscar)
            else:
                object_list = Citacion.objects.all()
            return render(request, "citacion/citacion_list.html", {'object_list': object_list})
        except ValueError:
            return render(request, "citacion/citacion_list.html")


class DetalleList(LoginRequiredMixin, DetailView):
    model = Citacion
    template_name = 'citacion/citacion.html'
