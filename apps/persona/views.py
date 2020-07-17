from django.shortcuts import redirect, render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.models import User
from django.http import HttpResponse
# from django.http import Http404
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from apps.persona.forms import PersonaForm
from apps.persona.models import Persona
from apps.proceso.models import Proceso


def lista(request):
    listas = serializers.serialize('json', User.objects.all(), fields=[
        'last_login', 'username', 'first_name', 'last_name', 'email'])
    return HttpResponse(listas, content_type='application/json')


def index_persona(request):
    return render(request, "persona/persona.html")


class PersonaList(LoginRequiredMixin, ListView):
    model = Persona
    template_name = 'persona/persona_list.html'
    paginate_by = 20


class PersonaCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'persona.add_persona'
    model = Persona
    form_class = PersonaForm
    template_name = 'persona/persona_form.html'
    success_error = "El numero de documento de identidad ya existe"

    def post(self, request, *args, **kwargs):
        try:
            if request.method == "POST":
                form = PersonaForm(request.POST)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.save()
                return redirect('persona:detalle', pk=post.pk)
        except UnboundLocalError:
            form = PersonaForm()
            messages.success(self.request, self.success_error)
            return render(request, "persona/persona_form.html", {'form': form})


class PersonaUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'persona.change_persona'
    model = Persona
    form_class = PersonaForm
    template_name = 'persona/persona_form.html'

    def get_success_url(self):
        value = self.kwargs['pk']
        return reverse_lazy('persona:detalle', kwargs={'pk': value})


class PersonaDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'persona.delete_persona'
    model = Persona
    template_name = 'persona/persona_delete.html'
    success_url = reverse_lazy('persona:listado')
    success_message = "ha sido eliminado exitosamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PersonaDelete, self).delete(request, *args, **kwargs)


class BuscarView(LoginRequiredMixin, ListView):
    model = Persona
    template_name = 'persona/persona_list.html'
    success_error = "consulta inexistentes"

    def post(self, request):
        try:
            buscar = request.POST['buscalo']
            if buscar != '':
                object_list = Persona.objects.filter(
                    documento__contains=buscar) | Persona.objects.filter(
                        nombre__contains=buscar) | Persona.objects.filter(
                            apellido__contains=buscar)
            else:
                object_list = Persona.objects.all()
            return render(request, "persona/persona_list.html", {'object_list': object_list})
        except ValueError:
            object_list = Persona.objects.all()
            messages.success(self.request, self.success_error)
            return render(request, "persona/persona_list.html", {'object_list': object_list})


class DetalleList(LoginRequiredMixin, DetailView):
    model = Persona
    template_name = 'persona/persona.html'


class ProcesosList(LoginRequiredMixin, ListView):
    model = Proceso
    template_name = 'proceso/proceso_list.html'

    def get_queryset(self):
        object_list = Proceso.objects.filter(
            demandado_id=self.kwargs['pk']) | Proceso.objects.filter(
                demandante_id=self.kwargs['pk'])
        return object_list
