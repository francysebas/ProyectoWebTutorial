from django.shortcuts import render, redirect
from .forms import FormularioContactos
from django.core.mail import send_mail, EmailMessage


# Create your views here.


def contacto(request):
    # instanciar el formulario
    formulario_contacto = FormularioContactos()

    # boton enviar-rescatar informacion de formulario
    if request.method == "POST":
        formulario_contacto = FormularioContactos(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            # enviar email
            email = EmailMessage("Mensaje desde app Django",
                                 "el usuario con nombre {} con la dirección {} escribe lo siguiente: \n\n {}".
                                 format(nombre, email, contenido), "", ["edilverllantenguerrero@gmail.com"],
                                 reply_to=[email])
            try:
                email.send()

                return redirect("/contacto/?valido")
            except:

                return redirect("/contacto/?novalido")

    return render(request, "contactoApp/contacto.html", {'miFormularioContacto': formulario_contacto})
