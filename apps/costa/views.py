from django.shortcuts import redirect, render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers

from django.db.models import Sum, F
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from apps.costa.forms import CostaForm
from apps.costa.models import Costa
from apps.abono.models import Abono


def lista(request):
    listas = serializers.serialize('json', User.objects.all())
    return HttpResponse(listas, content_type='application/json')


def index_costa(request):
    return render(request, "costa/costa.html")


class CostaList(LoginRequiredMixin, ListView):
    model = Costa
    template_name = 'costa/costa_list.html'
    paginate_by = 20


class CostaCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'costa.add_costa'
    model = Costa
    form_class = CostaForm
    template_name = 'costa/costa_form.html'
    success_error = "La costa de este proceso ya existe"

    def post(self, request, *args, **kwargs):
        try:
            if request.method == "POST":
                form = CostaForm(request.POST)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.save()
                return redirect('costa:detalle', pk=post.pk)
        except UnboundLocalError:
            form = CostaForm()
            messages.success(self.request, self.success_error)
            return render(request, 'costa/costa_form.html', {'form': form})


class CostaUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'costa.change_costa'
    model = Costa
    form_class = CostaForm
    template_name = 'costa/costa_form.html'

    def get_success_url(self):
        value = self.kwargs['pk']
        return reverse_lazy('costa:detalle', kwargs={'pk': value})


class CostaDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'costa.delete_costa'
    model = Costa
    template_name = 'costa/costa_delete.html'
    success_url = reverse_lazy('costa:listado')
    success_message = "ha sido eliminado exitosamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(CostaDelete, self).delete(request, *args, **kwargs)


class BuscarView(LoginRequiredMixin, ListView):
    model = Costa
    template_name = 'costa/costa_list.html'
    success_error = "consulta inexistentes"

    def post(self, request):
        try:
            buscar = request.POST['buscalo']
            if buscar != '':
                object_list = Costa.objects.filter(
                    proceso__radicado__contains=buscar) | Costa.objects.filter(
                        proceso__expediente=buscar) | Costa.objects.filter(
                        proceso__nombre=buscar)
            else:
                object_list = Costa.objects.all()
            return render(request, "costa/costa_list.html", {'object_list': object_list})
        except ValueError:
            object_list = Costa.objects.all()
            messages.success(self.request, self.success_error)
            return render(request, "costa/costa_list.html", {'object_list': object_list})


class DetalleList(LoginRequiredMixin, DetailView):
    model = Costa
    template_name = 'costa/costa.html'

    def get(self, request, *args, **kwargs):
        suma = Abono.objects.filter(costa=self.kwargs['pk']).aggregate(
            valor_sum=Sum('valor'))['valor_sum']
        Costa.objects.filter(proceso_id=self.kwargs['pk']).update(abonado=suma)
        Costa.objects.filter(proceso_id=self.kwargs['pk']).update(
            deuda=F('total')-F('abonado'))
        return super().get(request, *args, **kwargs)


class AbonosList(LoginRequiredMixin, ListView):
    model = Abono, Costa
    template_name = 'abono/abonos_list.html'

    def get_queryset(self):
        object_list = Abono.objects.filter(costa=self.kwargs['pk'])
        # suma = Abono.objects.filter(costa=self.kwargs['pk']).aggregate(
        #     valor_sum=Sum('valor'))['valor_sum']
        # Costa.objects.filter(id=self.kwargs['pk']).update(abonado=suma)
        # Costa.objects.filter(id=self.kwargs['pk']).update(
        #     deuda=F('total')-F('abonado'))
        return object_list
