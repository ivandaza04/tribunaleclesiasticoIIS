from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from apps.decreto.forms import DecretoForm
from apps.decreto.models import Decreto
# from apps.proceso.models import Proceso


def lista(request):
    listas = serializers.serialize('json', User.objects.all())
    return HttpResponse(listas, content_type='application/json')


class DecretoList(LoginRequiredMixin, ListView):
    model = Decreto
    template_name = 'decreto/decreto_list.html'

    def get_queryset(self):
        object_list = Decreto.objects.filter(
            proceso_id=self.kwargs['pk'])
        return object_list


class DecretoCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'decreto.add_decreto'
    model = Decreto
    form_class = DecretoForm
    template_name = 'decreto/decreto_form.html'

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = DecretoForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.proceso_id = self.kwargs['fk']
                post.save()
            return redirect('decreto:detalle', pk=post.pk)
        else:
            form = DecretoForm()
        return render('decreto/decreto_form.html', {'form': form})


class DecretoUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'decreto.change_decreto'
    model = Decreto
    form_class = DecretoForm
    template_name = 'decreto/decreto_form.html'

    def get_success_url(self):
        value = self.kwargs['pk']
        return reverse_lazy('decreto:detalle', kwargs={'pk': value})


class DecretoDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'decreto.delete_decreto'
    model = Decreto
    template_name = 'decreto/decreto_delete.html'
    success_url = reverse_lazy('proceso:listado')
    success_message = "ha sido eliminado exitosamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DecretoDelete, self).delete(request, *args, **kwargs)


class BuscarView(LoginRequiredMixin, ListView):
    model = Decreto
    template_name = 'decreto/decreto_list.html'

    def post(self, request):
        try:
            buscar = request.POST['buscalo']
            if buscar != '':
                object_list = Decreto.objects.filter(
                    proceso__expediente=buscar) | Decreto.objects.filter(
                        proceso__nombre=buscar) | Decreto.objects.filter(
                            decretos__nombre=buscar)
            else:
                object_list = Decreto.objects.all()
            return render(request, "decreto/decreto_list.html", {'object_list': object_list})
        except ValueError:
            return render(request, "decreto/decreto_list.html")


class DetalleList(LoginRequiredMixin, DetailView):
    model = Decreto
    template_name = 'decreto/decreto.html'
