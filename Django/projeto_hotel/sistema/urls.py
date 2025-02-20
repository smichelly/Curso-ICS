"""
URL configuration for sistema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from.views import home, aluguelcarro, lazerbemestar, cadastro, feedback, fazer_reserva, fazer_cadastro, coletar_feedback
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('aluguelcarro/', aluguelcarro),
    path('aluguelcarro/reservar/<int:carro_id>', fazer_reserva, name='reservar'),
    # url que chama uma view para o cadastro
    path('lazerbemestar/', lazerbemestar),
    path('cadastro/', cadastro, name="cadastro"),
    path('cadastrar', fazer_cadastro, name='fazer_cadastro'),
    path('feedback/', feedback),
    path('coletar-feedback/', coletar_feedback, name="coletar_feedback"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)