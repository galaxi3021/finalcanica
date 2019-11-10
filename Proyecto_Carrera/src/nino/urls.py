from django.urls import path

from . import views

app_name="nino"
urlpatterns = [
    path("general/",views.NNAListView.as_view(),name="list"),
    path("a_dental/",views.Area_DentalListView.as_view(),name="list_dental"),
    path("<int:pk>/", views.Area_DentalDetailView.as_view(), name="detail_dental"),
    path("a_psicologica/",views.Area_PsicologicaListView.as_view(),name="list_psicologica"),
    path("<int:pk>/psico", views.Area_PsicologicaDetailView.as_view(), name="detail_psi"),
    path("a_social/",views.Area_SocialListView.as_view(),name="list_social"),
    path("<int:pk>/social", views.Area_SocialDetailView.as_view(), name="detail_social"),
    path("a_medica/",views.Area_MedicaListView.as_view(),name="list_medica"),
    path("<int:pk>/medica", views.Area_MedicaDetailView.as_view(), name="detail_medico"),
    path("informe_medico/",views.Evaluacion_MedicaListView.as_view(),name="list_doctor"),
    path("<int:pk>/medic", views.Evaluacion_MedicaDetailView.as_view(), name="detail_doc"),
    path('menu/',views.reporteria,name="dashboard")

]