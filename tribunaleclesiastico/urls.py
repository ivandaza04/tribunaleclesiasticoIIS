"""tribunaleclesiastico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from django.contrib.staticfiles.urls import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
# from . import settings
# from apps.file import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('abono/', include('apps.abono.urls'), name='abono'),
    path('accion/', include('apps.accion.urls'), name='accion'),
    path('acta/', include('apps.acta.urls'), name='acta'),
    path('citacion/', include('apps.citacion.urls'), name='citacion'),
    path('colegiado/', include('apps.colegiado.urls'), name='colegiado'),
    path('costa/', include('apps.costa.urls'), name='costa'),
    path('declaracion/', include('apps.declaracion.urls'), name='declaracion'),
    path('declaraciontestigo/', include('apps.declaraciontestigo.urls'),
         name='declaraciontestigo'),
    path('decreto/', include('apps.decreto.urls'), name='decreto'),
    path('file/', include('apps.file.urls'), name='file'),
    # path('file/List/', views.FileList.as_view(), name='filelist'),
    path('persona/', include('apps.persona.urls'), name='persona'),
    path('proceso/', include('apps.proceso.urls'), name='proceso'),
    path('reporte/', include('apps.reporte.urls'), name='reporte'),
    path('sentencia/', include('apps.sentencia.urls'), name='sentencia'),
    path('testigo/', include('apps.testigo.urls'), name='testigo'),
    path('', include('apps.home.urls'), name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='usuario/login.html'), name='login'),
    path('reset/password_reset/', PasswordResetView.as_view(
        template_name='registration/password_reset_form.html'), name='password_reset'),
    path('reset/password_reset_done/', PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
