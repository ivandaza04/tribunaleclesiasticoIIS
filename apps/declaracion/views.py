from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from apps.declaracion.forms import DeclaracionForm
from apps.declaracion.models import Declaracion


def lista(request):
    listas = serializers.serialize('json', User.objects.all())
    return HttpResponse(listas, content_type='application/json')


class DeclaracionList(LoginRequiredMixin, ListView):
    model = Declaracion
    template_name = 'declaracion/declaracion_list.html'

    def get_queryset(self):
        object_list = Declaracion.objects.filter(
            proceso_id=self.kwargs['pk'])
        return object_list


class DeclaracionCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'declaracion.add_declaracion'
    model = Declaracion
    form_class = DeclaracionForm
    template_name = 'declaracion/declaracion_form.html'

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = DeclaracionForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.proceso_id = self.kwargs['fk']
                post.save()
            return redirect('declaracion:detalle', pk=post.pk)
        else:
            form = DeclaracionForm()
        return render('declaracion/declaracion_form.html', {'form': form})


class DeclaracionUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'declaracion.change_declaracion'
    model = Declaracion
    form_class = DeclaracionForm
    template_name = 'declaracion/declaracion_form.html'

    def get_success_url(self):
        value = self.kwargs['pk']
        return reverse_lazy('declaracion:detalle', kwargs={'pk': value})


class DeclaracionDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'declaracion.delete_declaracion'
    model = Declaracion
    template_name = 'declaracion/declaracion_delete.html'
    success_url = reverse_lazy('proceso:listado')
    success_message = "ha sido eliminado exitosamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeclaracionDelete, self).delete(request, *args, **kwargs)


class BuscarView(LoginRequiredMixin, ListView):
    model = Declaracion
    template_name = 'declaracion/declaracion_list.html'

    def post(self, request):
        try:
            buscar = request.POST['buscalo']
            if buscar != '':
                object_list = Declaracion.objects.filter(
                    proceso__expediente=buscar) | Declaracion.objects.filter(proceso__nombre=buscar)
            else:
                object_list = Declaracion.objects.all()
            return render(request, "declaracion/declaracion_list.html",
                          {'object_list': object_list})
        except ValueError:
            return render(request, "declaracion/declaracion_list.html")


class DetalleList(LoginRequiredMixin, DetailView):
    model = Declaracion
    template_name = 'declaracion/declaracion.html'
