from django.shortcuts import render
from app.forms import filmForm
from app.models import Filme

# Create your views here.

def index(request):
    obj =  Filme.objects.all()
    return render(request, 'index.html', {'obj': obj})


def form(request):
    if request.method == 'GET':
        form = filmForm()
        context = {'form': form}
        return render(request, 'form.html', context)
    else:
        form = filmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = filmForm()

        context = {'form': form}
        return render(request, 'form.html', {'form': form})