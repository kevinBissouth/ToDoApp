from django.shortcuts import render, redirect, get_object_or_404
from .forms import TacheForm
from .models import Tache

def index(request):
    return render(request, 'index.html')

def work(request):
    taches = Tache.objects.all().order_by('-id')  # du plus récent au plus ancien
    return render(request, 'workPage.html', {'taches': taches})


def add_tache(request):
    tache_sauvegarde = False

    if request.method == 'POST':
        form = TacheForm(request.POST)
        if form.is_valid():
            form.save()
            tache_sauvegarde = True
            form = TacheForm()  # Réinitialiser le formulaire
            return redirect('work')
    else:
        form = TacheForm()

    return render(request, 'addTache.html', {
        'form': form,
        'tache_sauvegarde': tache_sauvegarde
    })


def save_tache(request):
    if request.method == 'POST':
        form = TacheForm(request.POST)
        if form.is_valid():
            form.save()  
            form = TacheForm()  
    else:
        form = TacheForm()
    render(request, 'addTache.html', {'form': form})


def delete_tache(request, id):
    tache = get_object_or_404(Tache, id=id)
    if request.method == 'POST':
        tache.delete()
        return redirect('work')
    return render(request, 'confirmer_suppression.html' , {'tache' : tache})

def modifie_tache(request, id):
    tache = get_object_or_404(Tache, id=id)
    if request.method == 'POST':
        form = TacheForm(request.POST, instance=tache)
        if form.is_valid():
            form.save()
            return redirect('work')
    else:
        form = TacheForm(instance=tache)
    return render(request, 'modifieTache.html', {'form': form, 'tache': tache})

