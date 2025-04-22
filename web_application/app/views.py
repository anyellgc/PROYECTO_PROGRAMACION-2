from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import FormularioUsuario
from django.contrib.auth import authenticate, login
# Create your views here.
def registro(request):
    return render(request, 'app/registro.html')

@login_required
def inicio(request):
    return render(request, 'app/inicio.html')

def exit(request):
    logout(request)
    return redirect('registro')

def registrer(request):
    data = {
        'form': FormularioUsuario()
    }

    if request.method == 'POST':
        user_creation_form = FormularioUsuario(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password2'])
            login(request, user)

            return redirect('registro')

    return render(request, 'app/registrer.html', data)