"""
URL configuration for sistemaHistorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from App.login import LoginView
from App.views import *
from App.login import LogoutRedirectView


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',LoginView.as_view(), name='login'),
    path('home',HomeView.as_view(), name='home'),
    path('logout/',LogoutRedirectView.as_view(), name='logout'),
    path('home/pacientes',PacienteListView.as_view(), name='paciente_list'),
    path('home/pacientes/create',PacienteCreateView.as_view(), name='paciente_create'),
    path('home/pacientes/edit/<slug:slug>',PacienteEditView.as_view(), name='paciente_edit'),
    path('home/ficha_medica',Ficha_MedicaListView.as_view(), name='ficha_medica_list'),
    path('home/ficha_medica/create',Ficha_MedicaCreateView.as_view(), name='ficha_medica_create'),
    path('home/ficha_medica/edit/<slug:slug>',Ficha_MedicaEditView.as_view(), name='ficha_medica_edit'),

    path('home/consulta',ConsultaListView.as_view(), name='consulta_list'),
    path('home/consulta/create',ConsultaCreateView.as_view(), name='consulta_create'),
    path('home/consulta/edit/<slug:slug>',ConsultaEditView.as_view(), name='consulta_edit'),
]
