from django.urls import path
# from django.contrib.auth.decorators import login_required

from apps.home.views import formatos, delegacion, proteccion, EntradaList, DetalleList

app_name = 'home'
urlpatterns = [
    # path('', index, name='index'),
    path('formatos', formatos, name='formatos'),
    path('delegacion', delegacion, name='delegacion'),
    path('proteccion', proteccion, name='proteccion'),
    path('', EntradaList.as_view(), name='index'),
    path('blog/<pk>/', DetalleList.as_view(), name='blog'),
]
