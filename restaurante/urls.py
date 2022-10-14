"""restaurante URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from restauranteapp.views import index, salvar_mesa,mesas,editar_mesa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index,name='index'),
    path('salvar_mesa/', salvar_mesa,name='salvar_mesa'),
    path('mesas/', mesas,name='mesas'),
    path('editar_mesa/<int:id>', editar_mesa,name='editar_mesa'),
    re_path(r'^img/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
