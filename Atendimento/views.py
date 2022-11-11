from django.shortcuts import render
from django.views import generic
from .models import plano
from django.template import loader

from docx import Document

from django.http.response import HttpResponse

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
# Create your views here.

class Login(generic.ListView):
    model = plano
    template_name = 'Atendimento/templates/login.html'
    def get_queryset(self):
        return plano.objects.order_by('-created')

class IndexView(generic.ListView):
    model = plano
    template_name = 'Atendimento/templates/index.html'
    def get_queryset(self):
        return plano.objects.order_by('-created')

'''class CreateView(generic.ListView):
    model = plano
    template_name = 'Atendimento/templates/criarPlano.html'
    def get_queryset(self):
        return plano.objects.order_by('-created')'''


class CreatePdaView(CreateView):
    model = plano
    template_name = 'Atendimento/templates/criarPlano.html'
    fields = ['inquilino','sistema','demanda']
    success_url = reverse_lazy('index')
    def get_queryset(self):
        return plano.objects.order_by('-created')



def ver(request, pda_id):
    pda = plano.objects.filter(id=pda_id)
    pda = pda[0]
    template = loader.get_template('Atendimento/templates/pda.html')
    context = {
        'id': pda.id,
        'sistema': pda.sistema,
        'inquilino': pda.inquilino,
        'desc_produto': pda.desc_produto
    }
    return HttpResponse(template.render(context, request))




def editar(request, pk):
    pda_ed = plano.objects.filter(id=pk)
    template = loader.get_template('Atendimento/templates/editar.html')
    pda_ed = pda_ed[0]
    context = {
        'id': pda_ed.id,
        'sistema': pda_ed.sistema,
        'inquilino': pda_ed.inquilino,
        'desc_produto': pda_ed.desc_produto
    }

    return HttpResponse(template.render(context, request))


'''def criaWord(request,pk):
    pda_ed = plano.objects.filter(id=pk)
    pda_ed = pda_ed[0]

    context = {
        'id': pda_ed.id,
        'sistema': pda_ed.sistema
    }
    document = Document()
    document.add_heading('sistema', 0)
    document.save('demo.docx')

    template = loader.get_template('Atendimento/templates/editar.html')

    return HttpResponse(template.render(context, request))'''

def download_world(request,pk):
    pda_ed = plano.objects.filter(id=pk)
    pda_ed = pda_ed[0]
    context = {
        'id': pda_ed.id,
        'sistema': pda_ed.sistema

    }

    document = Document()
    document.add_heading('Proposta de atendimento', 0)
    document.add_paragraph('Sistema')
    document.add_paragraph( pda_ed.sistema)
    document.save('proposta.docx')

    template = loader.get_template('Atendimento/templates/download.html')
    return HttpResponse(template.render(context, request))




