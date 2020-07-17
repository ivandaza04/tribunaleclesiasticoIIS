from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.accion.views import DetalleList, BuscarView, AccionList
from apps.accion.views import AccionCreate, AccionUpdate, AccionDelete

app_name = 'accion'
urlpatterns = [
    path('detalle/<pk>/', login_required(DetalleList.as_view()), name='detalle'),
    path('buscar', login_required(BuscarView.as_view()), name='buscar'),
    path('registrar/<fk>/', login_required(AccionCreate.as_view()), name='registrar'),
    path('listado/<pk>/', AccionList.as_view(), name='listado'),
    path('actualizar/<pk>/', login_required(AccionUpdate.as_view()), name='actualizar'),
    path('eliminar/<pk>/', login_required(AccionDelete.as_view()), name='eliminar'),
]
