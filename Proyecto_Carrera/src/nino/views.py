from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import NNA,Area_Dental,Area_Psicologica,Area_Social,Area_Medica
from modulo_doctor.models import Evaluacion_Medica
# Create your views here.


class NNAListView(generic.ListView):
    model = NNA
    template_name = "list.html"


class NNADetailView(generic.DetailView):
    model = NNA
    template_name = "detail.html"


class Area_DentalListView(generic.ListView):
    model = Area_Dental
    template_name = "list_dental.html"


class Area_DentalDetailView(generic.DetailView):
    model = Area_Dental
    template_name = "detail_dental.html"


class Area_PsicologicaListView(generic.ListView):
    model = Area_Psicologica
    template_name = "list_psicologica.html"


class Area_PsicologicaDetailView(generic.DetailView):
    model = Area_Psicologica
    template_name = "detail_psi.html"


class Area_SocialListView(generic.ListView):
    model = Area_Social
    template_name = "list_social.html"


class Area_SocialDetailView(generic.DetailView):
    model = Area_Social
    template_name = "detail_social.html"

class Area_MedicaListView(generic.ListView):
    model = Area_Medica
    template_name = "list_medica.html"


class Area_MedicaDetailView(generic.DetailView):
    model = Area_Medica
    template_name = "detail_medico.html"

class Evaluacion_MedicaListView(generic.ListView):
    model = Evaluacion_Medica
    template_name = "list_doctor.html"


class Evaluacion_MedicaDetailView(generic.DetailView):
    model = Evaluacion_Medica
    template_name = "informe_medico.html"

def reporteria(request):
    return render(request,'dashboard.html')
