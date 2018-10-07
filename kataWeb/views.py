from django.shortcuts import render

from .models import Trabajador, TrabajadorForm, UserForm, Comentario
from .models import TiposDeServicio
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def index(request):
    trabajadores = Trabajador.objects.all()
    tipos_de_servicios = TiposDeServicio.objects.all()
    form_trabajador = TrabajadorForm(request.POST)
    form_usuario = UserForm(request.POST)

    context = {'trabajadores': trabajadores, 'tipos_de_servicios': tipos_de_servicios,
               'form_trabajador': form_trabajador, 'form_usuario': form_usuario, 'base_url': settings.STATIC_URL}
    return render(request, 'polls/index.html', context)

def editar_perfil(request,idTrabajador):
    trabajador=Trabajador.objects.get(usuarioId=idTrabajador)
    if request.method == 'POST':
        # formulario enviado
        form_trabajador = TrabajadorForm(request.POST, request.FILES, instance=trabajador)

        if form_trabajador.is_valid():
            # formulario validado correctamente
            form_trabajador.save()
            return HttpResponseRedirect('/')

    else:
        # formulario inicial
        form_trabajador = TrabajadorForm(instance=trabajador)

    context = {'form_trabajador': form_trabajador}
    return render(request, 'polls/editar.html', context)