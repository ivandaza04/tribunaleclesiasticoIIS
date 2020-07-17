from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from apps.acta.forms import ActaForm
from apps.acta.models import Acta


def lista(request):
    listas = serializers.serialize('json', User.objects.all())
    return HttpResponse(listas, content_type='application/json')


class ActaList(LoginRequiredMixin, ListView):
    model = Acta
    template_name = 'acta/acta_list.html'

    def get_queryset(self):
        object_list = Acta.objects.filter(
            proceso_id=self.kwargs['pk'])
        return object_list


class ActaCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'acta.add_acta'
    model = Acta
    form_class = ActaForm
    template_name = 'acta/acta_form.html'
    success_error = "El acta ya existe"

    def post(self, request, *args, **kwargs):
        try:
            if request.method == "POST":
                form = ActaForm(request.POST, request.FILES)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.proceso_id = self.kwargs['fk']
                    post.save()
                return redirect('acta:detalle', pk=post.pk)
        except UnboundLocalError:
            form = ActaForm()
            messages.success(self.request, self.success_error)
            return render(request, "acta/acta_form.html", {'form': form})


class ActaUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'acta.change_acta'
    model = Acta
    form_class = ActaForm
    template_name = 'acta/acta_form.html'

    def get_success_url(self):
        value = self.kwargs['pk']
        return reverse_lazy('acta:detalle', kwargs={'pk': value})


class ActaDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'acta.delete_acta'
    model = Acta
    template_name = 'acta/acta_delete.html'
    success_url = reverse_lazy('proceso:listado')
    success_message = "ha sido eliminado exitosamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ActaDelete, self).delete(request, *args, **kwargs)


class BuscarView(LoginRequiredMixin, ListView):
    model = Acta
    template_name = 'acta/acta_list.html'
    success_error = "consulta inexistentes"

    def post(self, request):
        try:
            buscar = request.POST['buscalo']
            if buscar != '':
                object_list = Acta.objects.filter(
                    proceso__expediente=buscar) | Acta.objects.filter(notario__nombre=buscar)
            else:
                object_list = Acta.objects.all()
            return render(request, "acta/acta_list.html", {'object_list': object_list})
        except ValueError:
            object_list = Acta.objects.all()
            messages.success(self.request, self.success_error)
            return render(request, "acta/acta_list.html", {'object_list': object_list})


class DetalleList(LoginRequiredMixin, DetailView):
    model = Acta
    template_name = 'acta/acta.html'
