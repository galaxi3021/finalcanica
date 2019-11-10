from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory
from .models import Producto,Categoria_Producto
# Create your views here.

class ProductoListView(generic.ListView):
    model = Producto
    template_name = "list_product.html"


class ProductoUpdateView(generic.UpdateView):
    model = Producto
    fields=['nombre_producto','unidades']
    template_name= "form.html"

    def list_product(request):
        return render(request,'list_product.html')
