from django.shortcuts import redirect, render

# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from apps.file.forms import FileForm
from apps.file.models import File


def lista(request):
    listas = serializers.serialize('json', User.objects.all())
    return HttpResponse(listas, content_type='application/json')


def index_file(request):
    return render(request, "file/file.html")


class FileList(LoginRequiredMixin, ListView):
    model = File
    template_name = 'file/file_list.html'

    def get_queryset(self):
        object_list = File.objects.filter(
            proceso_id=self.kwargs['pk'])
        return object_list


class FileCreate(LoginRequiredMixin, CreateView):
    model = File
    form_class = FileForm
    template_name = 'file/file_form.html'

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = FileForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
            return redirect('file:detalle', pk=post.pk)
        else:
            form = FileForm()
        return render('file/file_form.html', {'form': form})


class FileUpdate(LoginRequiredMixin, UpdateView):
    model = File
    form_class = FileForm
    template_name = 'file/file_form.html'

    def get_success_url(self):
        value = self.kwargs['pk']
        return reverse_lazy('file:detalle', kwargs={'pk': value})


class FileDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'file.delete_file'
    model = File
    template_name = 'file/file_delete.html'
    success_url = reverse_lazy('proceso:listado')
    success_message = "el documento ha sido eliminado exitosamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(FileDelete, self).delete(request, *args, **kwargs)


class BuscarView(LoginRequiredMixin, ListView):
    model = File
    template_name = 'file/file_list.html'

    def post(self, request):
        try:
            buscar = request.POST['buscalo']
            if buscar != '':
                object_list = File.objects.filter(
                    nombre=buscar)
            else:
                object_list = File.objects.all()
            return render(request, "file/file_list.html", {'object_list': object_list})
        except ValueError:
            return render(request, "file/file_list.html")


class DetalleList(LoginRequiredMixin, DetailView):
    model = File
    template_name = 'file/file.html'
