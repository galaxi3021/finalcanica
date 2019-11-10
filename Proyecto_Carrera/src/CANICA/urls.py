"""CANICA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from nino import  views
from noticia import views
#from modulo_doctor import views


urlpatterns = [
    path('', include('nino.urls')),
    path('noticia/', include('noticia.urls')),
    path('doctor/', include('modulo_doctor.urls')),
    path('inventario/', include('inventario.urls')),
    path('',views.index, name='index'),
    path('about/',views.about, name='about'),
    path('programas/',views.programas, name='programas'),
    path('contact/',views.contact, name='contact'),
    path('calendario/',views.calendario, name='calendario'),
    path('donar/',views.donar, name='donar'),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
