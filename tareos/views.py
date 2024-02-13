from django.shortcuts import render, redirect, get_object_or_404
from .models import Persona, DesempenoDiario
from .forms import PersonaForm, DesempenoForm, DesempenoEditForm

def persona_crud(request):
    personas = Persona.objects.all()

    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('persona_crud')
    else:
        form = PersonaForm()

    return render(request, 'persona_crud.html', {'personas': personas, 'form': form})

def desempeno_crud(request):
    personas = Persona.objects.all()
    
    if request.method == 'POST':
        if 'editar_puntuacion' in request.POST:
            desempeno_id = request.POST['editar_puntuacion']
            desempeno = get_object_or_404(DesempenoDiario, pk=desempeno_id)
            form = DesempenoEditForm(request.POST, instance=desempeno)
            if form.is_valid():
                form.save()
                return redirect('desempeno_crud')
        else:
            form = DesempenoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('desempeno_crud')
    else:
        form = DesempenoForm()

    return render(request, 'desempeno_crud.html', {'personas': personas, 'form': form})


def persona_desempeno_crud(request):
    personas = Persona.objects.all()
    desempenos = DesempenoDiario.objects.all()

    if request.method == 'POST':
        if 'persona_submit' in request.POST:
            persona_form = PersonaForm(request.POST)
            if persona_form.is_valid():
                persona_form.save()
        elif 'desempeno_submit' in request.POST:
            desempeno_form = DesempenoForm(request.POST)
            if desempeno_form.is_valid():
                desempeno_form.save()
    
    persona_form = PersonaForm()
    desempeno_form = DesempenoForm()

    return render(
        request,
        'persona_desempeno_crud.html',
        {'personas': personas, 'desempenos': desempenos, 'persona_form': persona_form, 'desempeno_form': desempeno_form}
    )