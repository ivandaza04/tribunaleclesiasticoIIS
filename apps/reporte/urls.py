from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.reporte.views import ReporteView

app_name = 'reporte'
urlpatterns = [
    path('reporte', login_required(ReporteView.as_view()), name='reporte'),
]
