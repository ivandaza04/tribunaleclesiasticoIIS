from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.abono.views import DetalleList, BuscarView, AbonoList
from apps.abono.views import AbonoCreate, AbonoUpdate, AbonoDelete

app_name = 'abono'
urlpatterns = [
    path('detalle/<pk>/', DetalleList.as_view(), name='detalle'),
    path('buscar', BuscarView.as_view(), name='buscar'),
    path('registrar/<fk>/', login_required(AbonoCreate.as_view()), name='registrar'),
    path('listado', login_required(AbonoList.as_view()), name='listado'),
    path('actualizar/<pk>/', login_required(AbonoUpdate.as_view()), name='actualizar'),
    path('eliminar/<pk>/', login_required(AbonoDelete.as_view()), name='eliminar'),
]