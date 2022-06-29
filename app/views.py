from django.shortcuts import redirect, render
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
            return redirect('app:index')

        context = {'form': form}
        return render(request, 'form.html', {'form': form})


def edit(request, id):
    obj = Filme.objects.get(id=id)
    if request.method == 'GET':
        form = filmForm(instance=obj)
        context = {'form': form}
        return render(request, 'form.html', context)
    else:
        form = filmForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            form = filmForm()
            return redirect('app:index')

        context = {'form': form}
        return render(request, 'form.html', {'form': form, 'obj': obj })
        

def delete(request, id):
    obj = Filme.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('app:index')
    context = {'obj': obj}
    return render(request, 'delete.html', context)


def update(request, id):
    obj = Filme.objects.get(id=id)
    obj 
