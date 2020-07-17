from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.citacion.views import DetalleList, BuscarView, CitacionList
from apps.citacion.views import CitacionCreate, CitacionUpdate, CitacionDelete

app_name = 'citacion'
urlpatterns = [
    path('detalle/<pk>/', login_required(DetalleList.as_view()), name='detalle'),
    path('buscar', login_required(BuscarView.as_view()), name='buscar'),
    path('registrar/<fk>/', login_required(CitacionCreate.as_view()), name='registrar'),
    path('listado/<pk>/', login_required(CitacionList.as_view()), name='listado'),
    path('actualizar/<pk>/', login_required(CitacionUpdate.as_view()), name='actualizar'),
    path('eliminar/<pk>/', login_required(CitacionDelete.as_view()), name='eliminar'),
]
