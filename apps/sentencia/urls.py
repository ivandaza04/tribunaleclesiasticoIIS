from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.sentencia.views import DetalleList, BuscarView, SentenciaList
from apps.sentencia.views import SentenciaCreate, SentenciaUpdate, SentenciaDelete

app_name = 'sentencia'
urlpatterns = [
    path('detalle/<pk>/', login_required(DetalleList.as_view()), name='detalle'),
    path('buscar', login_required(BuscarView.as_view()), name='buscar'),
    path('registrar/<fk>/', login_required(SentenciaCreate.as_view()), name='registrar'),
    path('listado/<pk>/', login_required(SentenciaList.as_view()), name='listado'),
    path('actualizar/<pk>/', login_required(SentenciaUpdate.as_view()), name='actualizar'),
    path('eliminar/<pk>/', login_required(SentenciaDelete.as_view()), name='eliminar'),
]
