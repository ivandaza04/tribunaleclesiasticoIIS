from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.persona.views import ProcesosList, BuscarView, DetalleList
from apps.persona.views import PersonaList, PersonaCreate, PersonaUpdate, PersonaDelete

app_name = 'persona'
urlpatterns = [
    path('proceso/<pk>/', login_required(ProcesosList.as_view()), name='proceso'),
    path('detalle/<pk>/', login_required(DetalleList.as_view()), name='detalle'),
    path('buscar', login_required(BuscarView.as_view()), name='buscar'),
    path('registrar', login_required(PersonaCreate.as_view()), name='registrar'),
    path('listado', login_required(PersonaList.as_view()), name='listado'),
    path('actualizar/<pk>/', login_required(PersonaUpdate.as_view()), name='actualizar'),
    path('eliminar/<pk>/', login_required(PersonaDelete.as_view()), name='eliminar'),
]