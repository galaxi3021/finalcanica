from django.urls import path

from . import views

app_name="inventario"
urlpatterns = [
    path("",views.ProductoListView.as_view(),name="list_product"),
    path("<int:pk>/", views.ProductoUpdateView.as_view(), name='form'),
]