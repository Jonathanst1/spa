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
from django.urls import path, include
from Atendimento import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required



urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',login_required(views.IndexView.as_view()), name='index'),
    path('novoplano/',login_required( views.CreatePdaView.as_view()), name='criarPlano'),
    path('<int:pda_id>/', views.ver, name='ver'),
    path('<int:pk>/atualizar/',login_required( views.UpdatePda.as_view()),  name='atualizar'),
    path('world/<int:pk>', views.download_world, name='world'),
    path('<int:pk>/desativar/', views.desativar, name='desativar'),
    path('<int:pk>/delete/',login_required(views.DeletePda.as_view()), name='del_pda'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('duplicate/<int:id>/', views.duplicate_model, name='duplicar'),
    path('<int:id>/versionar/', views.versionar, name='versionar')
    



    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

