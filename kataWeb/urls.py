from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url('editar/(?P<idTrabajador>\d+)$', views.editar_perfil, name='editar'),
    url('login', views.login),
    url('ingresar', views.ingresar),
    url('register', views.register),
    url('logout', views.logout),
    url('trabajador/(?P<pk>\d+)$', views.detail),
    url('detail', views.detalle_trabajador),
    url('addComment', views.add_comment),
    url('mostrarComentarios/(?P<idTrabajador>\d+)$', views.mostrarComentarios),
    url('mostrarTrabajadores/(?P<tipo>\w+)$', views.mostrarTrabajadores),
    url('mostrarTrabajadores', views.mostrarTrabajadores),
    url('tipoServicio/(?P<pk>\d+)$', views.getTiposDeServicio),
]
