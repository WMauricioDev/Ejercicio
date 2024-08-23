from django.shortcuts import render, redirect
from .models import Persona 
from .form import PersonaForm

# Create your views here.
def listarPersonas(request):
    personas = Persona.objects.all()
    return render(request,'listarPersonas.html', {'personas':personas})
def crearPersonas(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect(listarPersonas)
    else:
        form = PersonaForm()
        return render(request,'crearPersonas.html', {'form':form})
