from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.testigo.views import DetalleList, BuscarView, TestigoList
from apps.testigo.views import TestigoCreate, TestigoUpdate, TestigoDelete

app_name = 'testigo'
urlpatterns = [
    path('detalle/<pk>/', login_required(DetalleList.as_view()), name='detalle'),
    path('buscar', login_required(BuscarView.as_view()), name='buscar'),
    path('registrar', login_required(TestigoCreate.as_view()), name='registrar'),
    path('listado', login_required(TestigoList.as_view()), name='listado'),
    path('actualizar/<pk>/', login_required(TestigoUpdate.as_view()), name='actualizar'),
    path('eliminar/<pk>/', login_required(TestigoDelete.as_view()), name='eliminar'),
]
