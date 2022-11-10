"""SPA URL Configuration

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
from django.urls import path
from Atendimento import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('pdas/', views.IndexView.as_view(), name='index'),
    path('novoplano/', views.CreateView.as_view(), name='criarPlano'),
    path('<int:pda_id>/', views.ver, name='ver'),
    path('editar/<int:pk>', views.editar, name='editar'),
    path('world/<int:pk>', views.download_world, name='world')


    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

