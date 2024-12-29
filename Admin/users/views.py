from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from users.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from users.forms import UserEditForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from users.models import Avatar  # Importa tu modelo Avatar
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.forms import UserEditForm
from users.models import Avatar  # Importa tu modelo Avatar
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserRegisterForm

def login_request(request):

    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "APP/inicio.html")

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})

def register(request):
    msg_register = ""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            msg_register = "Usuario registrado con éxito"
            return render(request, "users/registro.html", {"form": UserRegisterForm(), "msg_register": msg_register})
        else:
            # Mostrar errores en consola
            print(form.errors)
            msg_register = "Error en los datos ingresados"
    else:
        form = UserRegisterForm()
    
    return render(request, "users/registro.html", {"form": form, "msg_register": msg_register})


@login_required
def editar_perfil(request):
    """Vista para editar perfil (datos de User) y actualizar la imagen en Avatar."""

    usuario = request.user
    
    # Intentamos obtener o crear el Avatar asociado al user.
    try:
        avatar = usuario.avatar  # Esto asume que en Avatar tienes: user = models.OneToOneField(User, related_name='avatar')
    except Avatar.DoesNotExist:
        avatar = Avatar.objects.create(user=usuario)

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario)
        
        if miFormulario.is_valid():
            # Guarda los datos del usuario (email, first_name, last_name, etc.)
            miFormulario.save()

            # Si se subió una imagen (campo 'imagen' en el form), la asignamos al Avatar
            if miFormulario.cleaned_data.get("imagen"):
                avatar.imagen = miFormulario.cleaned_data["imagen"]
                avatar.save()

            return render(request, "APP/inicio.html")
        else:
            # Para ver por qué falla la validación (si ocurre)
            print("Errores del formulario:", miFormulario.errors)
    else:
        # Carga el form con los datos actuales del usuario
        miFormulario = UserEditForm(instance=usuario)

    return render(
        request,
        "users/editar_usuario.html",
        {
            "mi_form": miFormulario,
            "usuario": usuario
        }
    )
class CambiarPassView (LoginRequiredMixin, PasswordChangeView):

    template_name = "users/cambiar_pass.html"
    success_url = reverse_lazy('EditarPerfil')