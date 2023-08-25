from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.home, name="home"),
    path("consulta1/", views.llamar_procedimiento, name="consulta1")
]
