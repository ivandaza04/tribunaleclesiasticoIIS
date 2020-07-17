from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.usuario.views import login_usuario, error_usuario, RegistroUsuario

app_name = 'usuario'
urlpatterns = [
    path('error', error_usuario, name='error'),
    path('login', login_usuario, name='login'),
    path('registrar', login_required(RegistroUsuario.as_view()), name='registrar'),
]
