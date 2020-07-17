from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.decreto.views import DetalleList, BuscarView, DecretoList
from apps.decreto.views import DecretoCreate, DecretoUpdate, DecretoDelete

app_name = 'decreto'
urlpatterns = [
    path('detalle/<pk>/', login_required(DetalleList.as_view()), name='detalle'),
    path('buscar', login_required(BuscarView.as_view()), name='buscar'),
    path('registrar/<fk>/', login_required(DecretoCreate.as_view()), name='registrar'),
    path('listado/<pk>/', login_required(DecretoList.as_view()), name='listado'),
    path('actualizar/<pk>/', login_required(DecretoUpdate.as_view()), name='actualizar'),
    path('eliminar/<pk>/', login_required(DecretoDelete.as_view()), name='eliminar'),
]
