from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm

def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('films:list_film')
    else:
        form = FilmForm()
    return render(request, 'films/add_film.html', {'form': form})

def list_films(request):
    films = Film.objects.all()
    return render(request, 'films/list_films.html', {'films': films})
