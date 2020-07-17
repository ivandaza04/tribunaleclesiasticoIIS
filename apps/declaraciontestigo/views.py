from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from apps.declaraciontestigo.forms import DeclaracionTestigoForm
from apps.declaraciontestigo.models import DeclaracionTestigo


def lista(request):
    listas = serializers.serialize('json', User.objects.all())
    return HttpResponse(listas, content_type='application/json')


class DeclaracionList(LoginRequiredMixin, ListView):
    model = DeclaracionTestigo
    template_name = 'declaraciontestigo/declaracion_list.html'

    def get_queryset(self):
        object_list = DeclaracionTestigo.objects.filter(
            proceso_id=self.kwargs['pk'])
        return object_list


class DeclaracionCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'declaraciontestigo.add_declaraciontestigo'
    model = DeclaracionTestigo
    form_class = DeclaracionTestigoForm
    template_name = 'declaraciontestigo/declaracion_form.html'

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = DeclaracionTestigoForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.proceso_id = self.kwargs['fk']
                post.save()
            return redirect('declaraciontestigo:detalle', pk=post.pk)
        else:
            form = DeclaracionTestigoForm()
        return render('declaraciontestigo/declaracion_form.html', {'form': form})


class DeclaracionUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'declaraciontestigo.change_declaraciontestigo'
    model = DeclaracionTestigo
    form_class = DeclaracionTestigoForm
    template_name = 'declaraciontestigo/declaracion_form.html'

    def get_success_url(self):
        Value = self.kwargs['pk']
        return reverse_lazy('declaraciontestigo:detalle', kwargs={'pk': Value})


class DeclaracionDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'declaraciontestigo.delete_declaraciontestigo'
    model = DeclaracionTestigo
    template_name = 'declaraciontestigo/declaracion_delete.html'
    success_url = reverse_lazy('proceso:listado')
    success_message = "ha sido eliminado exitosamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeclaracionDelete, self).delete(request, *args, **kwargs)


class BuscarView(LoginRequiredMixin, ListView):
    model = DeclaracionTestigo
    template_name = 'declaraciontestigo/declaracion_list.html'

    def post(self, request):
        try:
            buscar = request.POST['buscalo']
            if buscar != '':
                object_list = DeclaracionTestigo.objects.filter(
                    proceso__expediente=buscar) | DeclaracionTestigo.objects.filter(
                        proceso__nombre=buscar)
            else:
                object_list = DeclaracionTestigo.objects.all()
            return render(request, "declaraciontestigo/declaracion_list.html",
                          {'object_list': object_list})
        except ValueError:
            return render(request, "declaraciontestigo/declaracion_list.html")


class DetalleList(LoginRequiredMixin, DetailView):
    model = DeclaracionTestigo
    template_name = 'declaraciontestigo/declaracion.html'
