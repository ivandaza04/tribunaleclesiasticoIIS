from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.colegiado.views import DetalleList, BuscarView, IntegranteDelete
from apps.colegiado.views import IntegranteCreate, IntegranteList, IntegranteUpdate

app_name = 'colegiado'
urlpatterns = [
    path('detalle/<pk>/', login_required(DetalleList.as_view()), name='detalle'),
    path('buscar', login_required(BuscarView.as_view()), name='buscar'),
    path('registrar', login_required(IntegranteCreate.as_view()), name='registrar'),
    path('listado', login_required(IntegranteList.as_view()), name='listado'),
    path('actualizar/<pk>/', login_required(IntegranteUpdate.as_view()), name='actualizar'),
    path('eliminar/<pk>/', login_required(IntegranteDelete.as_view()), name='eliminar'),
]
