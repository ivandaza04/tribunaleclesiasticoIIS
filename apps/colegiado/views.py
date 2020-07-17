from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from apps.colegiado.forms import IntegranteForm
from apps.colegiado.models import Colegiado


def index_colegiado(request):
    return render(request, "colegiado/colegiado.html")


class IntegranteList(LoginRequiredMixin, ListView):
    model = Colegiado
    template_name = 'colegiado/integrante_list.html'
    paginate_by = 20


class IntegranteCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'colegiado.add_colegiado'
    model = Colegiado
    form_class = IntegranteForm
    template_name = 'colegiado/integrante_form.html'

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = IntegranteForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
            return redirect('colegiado:detalle', pk=post.pk)
        else:
            form = IntegranteForm()
        return render('colegiado/integrante_form.html', {'form': form})


class IntegranteUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'colegiado.change_colegiado'
    model = Colegiado
    form_class = IntegranteForm
    template_name = 'colegiado/integrante_form.html'

    def get_success_url(self):
        value = self.kwargs['pk']
        return reverse_lazy('colegiado:detalle', kwargs={'pk': value})


class IntegranteDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'colegiado.delete_colegiado'
    model = Colegiado
    template_name = 'colegiado/integrante_delete.html'
    success_url = reverse_lazy('colegiado:listado')
    success_message = "ha sido eliminado exitosamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(IntegranteDelete, self).delete(request, *args, **kwargs)


class BuscarView(LoginRequiredMixin, ListView):
    model = Colegiado
    template_name = 'colegiado/integrante_list.html'
    success_error = "consulta inexistentes"

    def post(self, request):
        try:
            buscar = request.POST['buscalo']
            if buscar != '':
                object_list = Colegiado.objects.filter(
                    nombre__contains=buscar)
            else:
                object_list = Colegiado.objects.all()
            return render(request, "colegiado/integrante_list.html", {'object_list': object_list})
        except ValueError:
            object_list = Colegiado.objects.all()
            messages.success(self.request, self.success_error)
            return render(request, "colegiado/integrante_list.html", {'object_list': object_list})


class DetalleList(LoginRequiredMixin, DetailView):
    model = Colegiado
    template_name = 'colegiado/colegiado.html'
