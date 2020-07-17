from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.acta.views import DetalleList, BuscarView, ActaCreate, ActaList, ActaUpdate, ActaDelete

app_name = 'acta'
urlpatterns = [
    path('detalle/<pk>/', login_required(DetalleList.as_view()), name='detalle'),
    path('buscar', login_required(BuscarView.as_view()), name='buscar'),
    path('registrar/<fk>/', login_required(ActaCreate.as_view()), name='registrar'),
    path('listado/<pk>/', login_required(ActaList.as_view()), name='listado'),
    path('actualizar/<pk>/', login_required(ActaUpdate.as_view()), name='actualizar'),
    path('eliminar/<pk>/', login_required(ActaDelete.as_view()), name='eliminar'),
]
