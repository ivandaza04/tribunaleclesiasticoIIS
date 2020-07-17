from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.proceso.views import Consulta, Actividad, BuscarView, ProcesoList
from apps.proceso.views import ProcesoCreate, ProcesoUpdate, ProcesoDelete, DetalleList

app_name = 'proceso'
urlpatterns = [
    path('detalle/<pk>/', login_required(DetalleList.as_view()), name='detalle'),
    path('actividad/<pk>/', Actividad.as_view(), name='actividad'),
    path('buscar', login_required(BuscarView.as_view()), name='buscar'),
    path('registrar', login_required(ProcesoCreate.as_view()), name='registrar'),
    path('listado', login_required(ProcesoList.as_view()), name='listado'),
    path('actualizar/<pk>/', login_required(ProcesoUpdate.as_view()), name='actualizar'),
    path('consulta', Consulta.as_view(), name='consulta'),
    path('eliminar/<pk>/', login_required(ProcesoDelete.as_view()), name='eliminar'),
]
