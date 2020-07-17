from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.file.views import DetalleList, BuscarView, FileList, FileCreate, FileUpdate, FileDelete

app_name = 'file'
urlpatterns = [
    path('detalle/<pk>/', login_required(DetalleList.as_view()), name='detalle'),
    path('buscar', login_required(BuscarView.as_view()), name='buscar'),
    path('registrar', login_required(FileCreate.as_view()), name='registrar'),
    path('listado/<pk>/', login_required(FileList.as_view()), name='listado'),
    path('actualizar/<pk>/', login_required(FileUpdate.as_view()), name='actualizar'),
    path('eliminar/<pk>/', login_required(FileDelete.as_view()), name='eliminar'),
]
