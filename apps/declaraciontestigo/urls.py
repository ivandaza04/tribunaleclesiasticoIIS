from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.declaraciontestigo.views import DetalleList, BuscarView, DeclaracionList
from apps.declaraciontestigo.views import DeclaracionCreate, DeclaracionUpdate, DeclaracionDelete

app_name = 'declaraciontestigo'
urlpatterns = [
    path('detalle/<pk>/', login_required(DetalleList.as_view()), name='detalle'),
    path('buscar', login_required(BuscarView.as_view()), name='buscar'),
    path('registrar/<fk>/', login_required(DeclaracionCreate.as_view()), name='registrar'),
    path('listado/<pk>/', login_required(DeclaracionList.as_view()), name='listado'),
    path('actualizar/<pk>/', login_required(DeclaracionUpdate.as_view()), name='actualizar'),
    path('eliminar/<pk>/', login_required(DeclaracionDelete.as_view()), name='eliminar'),
]
