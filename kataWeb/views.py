from django.shortcuts import render

from .models import Trabajador, TrabajadorForm, UserForm, Comentario, User
from .models import TiposDeServicio
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib import auth

# Create your views here.

@csrf_exempt
def index(request):
    trabajadores = Trabajador.objects.all()
    tipos_de_servicios = TiposDeServicio.objects.all()
    form_trabajador = TrabajadorForm(request.POST)
    form_usuario = UserForm(request.POST)

    context = {'trabajadores': trabajadores, 'tipos_de_servicios': tipos_de_servicios,
               'form_trabajador': form_trabajador, 'form_usuario': form_usuario, 'base_url': settings.STATIC_URL}
    return render(request, 'polls/index.html', context)

@csrf_exempt
def login(request):
    username = request.POST.get('usrname', '')
    password = request.POST.get('psw', '')
    user = auth.authenticate(username=username, password=password)
    print('login--->' + username)
    if user is not None:
        auth.login(request, user)
        messages.success(request, "Bienvenido al sistema {}".format(username), extra_tags="alert-success")
        return HttpResponseRedirect('/')
    else:
        messages.error(request, "¡El usuario o la contraseña son incorrectos!", extra_tags="alert-danger")
        return HttpResponseRedirect('/')

@csrf_exempt
def logout(request):
    auth.logout(request)
    messages.info(request, "Cerraste sesión exitosamente", extra_tags="alert-info")
    return HttpResponseRedirect('/')

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username, password=password)
        user.first_name = request.POST.get('nombre')
        user.last_name = request.POST.get('apellidos')
        user.email = request.POST.get('correo')
        user.save()
        nuevo_trabajador = Trabajador(nombre=request.POST['nombre'],
                                      apellidos=request.POST['apellidos'],
                                      aniosExperiencia=request.POST.get('aniosExperiencia'),
                                      tiposDeServicio=TiposDeServicio.objects.get(pk=request.POST.get('tiposDeServicio')),
                                      telefono=request.POST.get('telefono'),
                                      correo=request.POST.get('correo'),
                                      imagen=request.POST.get('imagen'),
                                      usuarioId=user)
        nuevo_trabajador.save()

    return HttpResponseRedirect('/')


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

@csrf_exempt
def add_comment(request):
    if request.method == 'POST':
       new_comment = Comentario(texto=request.POST.get('texto'),
                                      trabajador=Trabajador.objects.get(pk=request.POST.get('trabajador')),
                                      correo=request.POST.get('correo'))
       new_comment.save()
    return HttpResponse(serializers.serialize("json", [new_comment]))

@csrf_exempt
def mostrarTrabajadores(request, tipo=""):
    if tipo == "":
      lista_trabajadores = Trabajador.objects.all()
    else:
      lista_trabajadores = Trabajador.objects.select_related().filter(tiposDeServicio__nombre__icontains=tipo)


    return HttpResponse(serializers.serialize("json", lista_trabajadores))

@csrf_exempt
def mostrarComentarios(request, idTrabajador):
    lista_comentarios =Comentario.objects.filter(trabajador=Trabajador.objects.get(pk=idTrabajador))

    return HttpResponse(serializers.serialize("json", lista_comentarios))
@csrf_exempt
def getTiposDeServicio(request, pk):
    tipo = TiposDeServicio.objects.get(pk=pk)
    return HttpResponse(serializers.serialize("json", [tipo]))
@csrf_exempt
def detalle_trabajador(request):
    return render(request, "polls/detalle.html")

@csrf_exempt
def detail(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    return HttpResponse(serializers.serialize("json", [trabajador]))

@csrf_exempt
def ingresar(request):
    return render(request, 'polls/login.html')