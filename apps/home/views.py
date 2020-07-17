from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from apps.home.models import Entrada


def index(request):
    return render(request, "home/index.html")


def formatos(request):
    return render(request, "home/formatos.html")


def delegacion(request):
    return render(request, "home/delegacion.html")


def proteccion(request):
    return render(request, "home/proteccion.html")


class EntradaList(ListView):
    model = Entrada
    template_name = 'home/index.html'
    paginate_by = 10


class DetalleList(DetailView):
    model = Entrada
    template_name = 'home/blog.html'
