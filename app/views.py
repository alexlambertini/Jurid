from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render
from app.forms import filmForm
from app.models import Filme 
from django.views.generic import ListView
from django.db.models import Q

# Create your views here.

def index(request):
    obj =  Filme.objects.all().order_by('-id')
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
        context = {'form': form, 'obj': obj}
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
            try:
                obj.delete()
            except:
                return HttpResponse('Erro ao deletar')
    context = {'obj': obj}
    return render(request, 'delete.html', context)



class SearchResultsView(ListView):
    model = Filme
    template_name = 'busca.html'
    
    def get_queryset(self): 

        query = self.request.GET.get("q")

        object_list = Filme.objects.filter(
            Q(titulo__icontains=query) | Q(ano__icontains=query) | Q(diretor__icontains=query) | Q(genero__icontains=query) | Q(classificacao__icontains=query) | Q(duracao__icontains=query) | Q(sinopse__icontains=query)
        )
        
        return object_list
