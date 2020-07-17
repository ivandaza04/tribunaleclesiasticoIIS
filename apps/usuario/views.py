import json
from rest_framework.views import APIView
# from django.shortcuts import render, resolve_url

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import CreateView
# from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
# from django.contrib import messages
# from django.conf import settings

from apps.usuario.forms import RegistroForm
from apps.usuario.serializers import UserSerializer


# Create your views here.


# def error_usuario(request):
#     return render(request, "usuario/error.html")


# def login_usuario(request):
#     return render(request, "usuario/login.html")


class login_usuario(LoginView):
    template_name = 'usuario/login.html'
    # success_url = reverse_lazy('proceso:listado')
    success_message = "Ha iniciado sesión exitosamente"
    success_error = "Su nombre de usuario o contraseña no son correcto."

    # def get_success_url(self):
    #     url = self.get_redirect_url()
    #     messages.success(self.get_redirect_url(), self.success_message)
    #     return url or resolve_url(settings.LOGIN_REDIRECT_URL)


class RegistroUsuario(PermissionRequiredMixin, CreateView):
    permission_required = 'apps.can_create_usuario'
    model = User
    template_name = 'usuario/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('home:index')


class UserAPI(APIView):
    serializer = UserSerializer

    def get(self, request):
        lista = User.objects.all()
        response = self.serializer(lista, many=True)
        return HttpResponse(json.dumps(response.data), content_type='application/json')
