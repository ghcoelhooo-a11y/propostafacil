# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("clientes/", views.cliente_list, name="cliente_list"),
]
