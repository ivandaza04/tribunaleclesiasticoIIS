from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from apps.accion.forms import AccionForm
from apps.accion.models import Accion


def lista(request):
    listas = serializers.serialize('json', User.objects.all())
    return HttpResponse(listas, content_type='application/json')


class AccionList(LoginRequiredMixin, ListView):
    model = Accion
    template_name = 'accion/accion_list.html'

    def get_queryset(self):
        object_list = Accion.objects.filter(
            proceso_id=self.kwargs['pk'])
        return object_list


class AccionCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'accion.add_accion'
    model = Accion
    form_class = AccionForm
    template_name = 'accion/accion_form.html'

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = AccionForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.proceso_id = self.kwargs['fk']
                post.save()
            return redirect('accion:detalle', pk=post.pk)
        else:
            form = AccionForm()
        return render('accion/accion_form.html', {'form': form})


class AccionUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'accion.change_accion'
    model = Accion
    form_class = AccionForm
    template_name = 'accion/accion_form.html'
    success_url = reverse_lazy('accion:listado')

    def get_success_url(self):
        value = self.kwargs['pk']
        return reverse_lazy('accion:detalle', kwargs={'pk': value})


class AccionDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'accion.delete_accion'
    model = Accion
    template_name = 'accion/accion_delete.html'
    success_url = reverse_lazy('proceso:listado')
    success_message = "ha sido eliminado exitosamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AccionDelete, self).delete(request, *args, **kwargs)


class BuscarView(LoginRequiredMixin, ListView):
    model = Accion
    template_name = 'accion/accion_list.html'
    success_error = "consulta inexistentes"

    def post(self, request):
        try:
            buscar = request.POST['buscalo']
            if buscar != '':
                object_list = Accion.objects.filter(
                    proceso__expediente=buscar) | Accion.objects.filter(
                        proceso__nombre=buscar) | Accion.objects.filter(accion__nombre=buscar)
            else:
                object_list = Accion.objects.all()
            return render(request, "accion/accion_list.html", {'object_list': object_list})
        except ValueError:
            object_list = Accion.objects.all()
            messages.success(self.request, self.success_error)
            return render(request, "accion/accion_list.html", {'object_list': object_list})


class DetalleList(LoginRequiredMixin, DetailView):
    model = Accion
    template_name = 'accion/accion.html'
