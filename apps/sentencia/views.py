from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from apps.sentencia.forms import SentenciaForm
from apps.sentencia.models import Sentencia


def lista(request):
    listas = serializers.serialize('json', User.objects.all())
    return HttpResponse(listas, content_type='application/json')


class SentenciaList(LoginRequiredMixin, ListView):
    model = Sentencia
    template_name = 'sentencia/sentencia_list.html'

    def get_queryset(self):
        object_list = Sentencia.objects.filter(
            proceso_id=self.kwargs['pk'])
        return object_list


class SentenciaCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'sentencia.add_sentencia'
    model = Sentencia
    form_class = SentenciaForm
    template_name = 'sentencia/sentencia_form.html'

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = SentenciaForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.proceso_id = self.kwargs['fk']
                post.save()
            return redirect('sentencia:detalle', pk=post.pk)
        else:
            form = SentenciaForm()
        return render('sentencia/sentencia_form.html', {'form': form})


class SentenciaUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'sentencia.change_sentencia'
    model = Sentencia
    form_class = SentenciaForm
    template_name = 'sentencia/sentencia_form.html'

    def get_success_url(self):
        value = self.kwargs['pk']
        return reverse_lazy('sentencia:detalle', kwargs={'pk': value})


class SentenciaDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'sentencia.delete_sentencia'
    model = Sentencia
    template_name = 'sentencia/sentencia_delete.html'
    success_url = reverse_lazy('proceso:listado')
    success_message = "ha sido eliminado exitosamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(SentenciaDelete, self).delete(request, *args, **kwargs)


class BuscarView(LoginRequiredMixin, ListView):
    model = Sentencia
    template_name = 'sentencia/sentencia_list.html'
    success_error = "consulta inexistentes"

    def post(self, request):
        try:
            buscar = request.POST['buscalo']
            if buscar != '':
                object_list = Sentencia.objects.filter(
                    proceso__expediente=buscar) | Sentencia.objects.filter(proceso__nombre=buscar)
            else:
                object_list = Sentencia.objects.all()
            return render(request, "sentencia/sentencia_list.html", {'object_list': object_list})
        except ValueError:
            object_list = Sentencia.objects.all()
            messages.success(self.request, self.success_error)
            return render(request, "sentencia/sentencia_list.html", {'object_list': object_list})


class DetalleList(LoginRequiredMixin, DetailView):
    model = Sentencia
    template_name = 'sentencia/sentencia.html'
