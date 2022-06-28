from multiprocessing import context
from django.shortcuts import render
from app.forms import filmForm

# Create your views here.

def index(request):
    return render(request, 'index.html')


def form(request):
    form = filmForm()
    context = {'form': form}
    return render(request, 'form.html', context)