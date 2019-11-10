from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Noticia
# Create your views here.

class NoticiaListView(generic.ListView):
    model = Noticia
    template_name = "noticia.html"


class NoticiaDetailView(generic.DetailView):
    model = Noticia
    template_name = "detail.html"


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def programas(request):
    return render(request, 'programas.html')

def contact(request):
    return render(request, 'contact.html')

def calendario(request):
    return render(request, 'calendario.html')

def donar(request):
    return render(request, 'donar.html')

