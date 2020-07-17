from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.costa.views import AbonosList, DetalleList, BuscarView, CostaList
from apps.costa.views import CostaCreate, CostaUpdate, CostaDelete

app_name = 'costa'
urlpatterns = [
    path('abonos/<pk>/', login_required(AbonosList.as_view()), name='abonos'),
    path('detalle/<pk>/', login_required(DetalleList.as_view()), name='detalle'),
    path('buscar', login_required(BuscarView.as_view()), name='buscar'),
    path('registrar', login_required(CostaCreate.as_view()), name='registrar'),
    path('listado', login_required(CostaList.as_view()), name='listado'),
    path('actualizar/<pk>/', login_required(CostaUpdate.as_view()), name='actualizar'),
    path('eliminar/<pk>/', login_required(CostaDelete.as_view()), name='eliminar'),
]