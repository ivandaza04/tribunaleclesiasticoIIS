from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from apps.testigo.forms import TestigoForm
from apps.testigo.models import Testigo


def lista(request):
    listas = serializers.serialize('json', User.objects.all())
    return HttpResponse(listas, content_type='application/json')


def index_Testigo(request):
    return render(request, "testigo/testigo.html")


class TestigoList(LoginRequiredMixin, ListView):
    model = Testigo
    template_name = 'testigo/testigo_list.html'
    paginate_by = 20


class TestigoCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'testigo.add_testigo'
    model = Testigo
    form_class = TestigoForm
    template_name = 'testigo/testigo_form.html'

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = TestigoForm(request.POST)
            if form.is_valid():
                post = form.save()
                post.save()
            return redirect('testigo:detalle', pk=post.pk)
        else:
            form = TestigoForm()
        return render('testigo/testigo_form.html', {'form': form})


class TestigoUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'testigo.change_testigo'
    model = Testigo
    form_class = TestigoForm
    template_name = 'testigo/testigo_form.html'

    def get_success_url(self):
        value = self.kwargs['pk']
        return reverse_lazy('testigo:detalle', kwargs={'pk': value})


class TestigoDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'testigo.delete_testigo'
    model = Testigo
    template_name = 'testigo/testigo_delete.html'
    success_url = reverse_lazy('testigo:listado')
    success_message = "ha sido eliminado exitosamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(TestigoDelete, self).delete(request, *args, **kwargs)


class BuscarView(LoginRequiredMixin, ListView):
    model = Testigo
    template_name = 'testigo/testigo_list.html'
    success_error = "consulta inexistentes"

    def post(self, request):
        try:
            buscar = request.POST['buscalo']
            if buscar != '':
                object_list = Testigo.objects.filter(
                    nombre__contains=buscar) | Testigo.objects.filter(apellidos__contains=buscar)
            else:
                object_list = Testigo.objects.all()
            return render(request, "testigo/testigo_list.html", {'object_list': object_list})
        except ValueError:
            object_list = Testigo.objects.all()
            messages.success(self.request, self.success_error)
            return render(request, "testigo/testigo_list.html", {'object_list': object_list})


class DetalleList(LoginRequiredMixin, DetailView):
    model = Testigo
    template_name = 'testigo/testigo.html'
