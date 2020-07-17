from django.shortcuts import redirect, render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from apps.abono.forms import AbonoForm
from apps.abono.models import Abono


def lista(request):
    listas = serializers.serialize('json', User.objects.all())
    return HttpResponse(listas, content_type='application/json')


def index_abono(request):
    return render(request, "abono/abono.html")


class AbonoList(LoginRequiredMixin, ListView):
    model = Abono
    template_name = 'abono/abono_list.html'


class AbonoCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'abono.add_abono'
    model = Abono
    form_class = AbonoForm
    template_name = 'abono/abono_form.html'

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = AbonoForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.costa_id = self.kwargs['fk']
                post.save()
            return redirect('abono:detalle', pk=post.pk)
        else:
            form = AbonoForm()
        return render('abono/abono_form.html', {'form': form})


class AbonoUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'abono.change_abono'
    model = Abono
    form_class = AbonoForm
    template_name = 'abono/abono_form.html'

    def get_success_url(self):
        value = self.kwargs['pk']
        return reverse_lazy('abono:detalle', kwargs={'pk': value})


class AbonoDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'abono.delete_abono'
    model = Abono
    template_name = 'abono/abono_delete.html'
    success_url = reverse_lazy('costa:listado')
    success_message = "ha sido eliminado exitosamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AbonoDelete, self).delete(request, *args, **kwargs)


class BuscarView(LoginRequiredMixin, ListView):
    model = Abono
    template_name = 'abono/abono_list.html'
    success_error = "consulta inexistentes"

    def post(self, request):
        try:
            buscar = request.POST['buscalo']
            if buscar != '':
                object_list = Abono.objects.filter(costa__numero=buscar)
            else:
                object_list = Abono.objects.all()
            return render(request, "abono/abono_list.html", {'object_list': object_list})
        except ValueError:
            object_list = Abono.objects.all()
            messages.success(self.request, self.success_error)
            return render(request, "abono/abono_list.html")


class DetalleList(LoginRequiredMixin, DetailView):
    model = Abono
    template_name = 'abono/abono.html'
