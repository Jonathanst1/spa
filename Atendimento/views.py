from django.shortcuts import render
from django.views import generic
from .models import plano
from django.template import loader
from django.contrib import messages

from docx import Document

from django.http.response import HttpResponse

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
# Create your views here.

class Login(generic.ListView):
    model = plano
    template_name = 'Atendimento/templates/login.html'


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

# classe para criar o pda
class CreatePdaView(CreateView):
    model = plano
    CHOICES = plano.CHOICES
    template_name = 'Atendimento/templates/criarPlano.html'
    fields = ['versao', 'sistema', 'inquilino',  'sub_demanda','demanda',
              'desc_produto', 'n_contrato', 'aditivo', 'ans',
              'necessidades', 'requisitos_LDPA', 'solucoes_impactadas',
              'anexo_contexto', 'telas_sistema', 'cronograma_implantacao','canais','n1','n2','area_solicitante_cliente',
              'obs_solicitante_cliente','area_executora_cliente','obs_executora_cliente',
              'area_solicitante_usuario','obs_solicitante_usuario','area_executora_usuario',
              'obs_executora_usuario','area_solicitante_base','publicacao_solicitante_base','obs_solicitante_base',
              'area_executora_base','publicacao_executora_base','obs_executora_base','area_solicitante_itens',
              'obs_solicitante_itens','area_executora_itens','obs_executora_itens','area_solicitante_cadastro_clientes',
              'area_executora_cadastro_clientes','obs_executora_cliente','obs_executora_cadastro_clientes','obs_solicitante_cadastro_clientes','area_solicitante_cadastro_base',
              'publicacao_executora_cadastro_base','publicacao_solicitante_cadastro_base','obs_solicitante_cadastro_base','area_executora_cadastro_base',
              'obs_executora_cadastro_base','area_responsavel_capacitacao','atendimento','carga_horaria','cronograma','obs_risco',
                'adequacao','capacitacao','responsavel']

    success_url = reverse_lazy('index')
    def get_queryset(self):
        return plano.objects.order_by('-created')


# função para visualização
def ver(request, pda_id):
    pda = plano.objects.filter(id=pda_id)
    pda = pda[0]
    template = loader.get_template('Atendimento/templates/pda.html')
    context = {
        'id': pda.id,
        'sistema': pda.sistema,
        'inquilino': pda.inquilino,
        'desc_produto': pda.desc_produto,
        'CHOICES': pda.CHOICES,
        'CHOICES2': pda.CHOICES2,
        'versao': pda.versao,
        'status': pda.status,
        'created': pda.created,
        'modified': pda.modified,
        'demanda': pda.demanda,
        'sub_demanda': pda.sub_demanda,
        'n_contrato' : pda.n_contrato,
        'aditivo': pda.aditivo,
        'ans': pda.ans,
        'necessidades': pda.necessidades,
        'requisitos_LDPA': pda.requisitos_LDPA,
        'solucoes_impactadas': pda.solucoes_impactadas,
        'anexo_contexto': pda.anexo_contexto,
        'telas_sistema' : pda.telas_sistema,
        'cronograma_implantacao' : pda.cronograma_implantacao,
        'canais' : pda.canais,
        'n1': pda.n1,
        'n2' : pda.n2,
        'adequacao': pda.adequacao,
        'area_solicitante_cliente': pda.area_solicitante_cliente,
        'obs_solicitante_cliente': pda.obs_solicitante_cliente,
        'area_executora_cliente': pda.area_executora_cliente,
        'obs_executora_cliente': pda.obs_executora_cliente,
        'area_solicitante_usuario': pda.area_solicitante_usuario,
        'obs_solicitante_usuario': pda.obs_solicitante_usuario,
        'area_executora_usuario': pda.area_executora_usuario,
        'obs_executora_usuario': pda.obs_executora_usuario,
        'area_solicitante_base': pda.area_solicitante_base,
        'publicacao_solicitante_base' : pda.publicacao_solicitante_base,
        'obs_solicitante_base': pda.obs_solicitante_base,
        'area_executora_base': pda.area_executora_base,
        'publicacao_executora_base': pda.publicacao_executora_base,
        'obs_executora_base': pda.obs_executora_base,
        'area_solicitante_itens': pda.area_solicitante_itens,
        'obs_solicitante_itens': pda.obs_solicitante_itens,
        'area_executora_itens': pda.area_executora_itens,
        'area_solicitante_cadastro_clientes': pda.area_solicitante_cadastro_clientes,
        'area_executora_cadastro_clientes': pda.area_executora_cadastro_clientes,
        'obs_executora_cadastro_clientes': pda.obs_executora_cadastro_clientes,
        'area_solicitante_cadastro_base': pda.area_solicitante_cadastro_base,
        'publicacao_solicitante_cadastro_base': pda.publicacao_solicitante_cadastro_base,
        'obs_solicitante_cadastro_base':pda.obs_solicitante_cadastro_base,
        'area_executora_cadastro_base':pda.area_executora_cadastro_base,
        'publicacao_executora_cadastro_base': pda.publicacao_executora_cadastro_base,
        'obs_executora_cadastro_base': pda.obs_executora_cadastro_base,
        'capacitacao': pda.capacitacao,
        'area_responsavel_capacitacao': pda.area_responsavel_capacitacao,
        'atendimento': pda.atendimento,
        'carga_horaria': pda.carga_horaria,
        'cronograma': pda.cronograma,
        'obs_risco': pda.obs_risco,
        'responsavel': pda.responsavel,
        'obs_executora_itens':pda.obs_executora_itens,
        'obs_solicitante_cadastro_clientes':pda.obs_solicitante_cadastro_clientes
        



    }
    return HttpResponse(template.render(context, request))

# classe para atualizar o pda
class UpdatePda(UpdateView):
    model = plano
    template_name = 'Atendimento/templates/atualizar.html'
    fields = ['versao', 'sistema','inquilino','demanda','sub_demanda',
              'desc_produto','n_contrato','aditivo','ans',
              'necessidades','requisitos_LDPA','solucoes_impactadas',
              'anexo_contexto','telas_sistema','cronograma_implantacao',
              'canais','n1','n2',  'area_solicitante_cliente',
              'obs_solicitante_cliente','area_executora_cliente','obs_executora_cliente',
              'area_solicitante_usuario','obs_solicitante_usuario','area_executora_usuario',
              'obs_executora_usuario','area_solicitante_base','obs_solicitante_base',
              'area_executora_base','publicacao_executora_base','obs_executora_base','area_solicitante_itens',
              'obs_solicitante_itens','area_executora_itens','obs_executora_itens','area_solicitante_cadastro_clientes',
              'area_executora_cadastro_clientes','obs_executora_cliente','area_solicitante_cadastro_base',
              'publicacao_executora_cadastro_base','obs_solicitante_cadastro_base','area_executora_cadastro_base',
              'publicacao_executora_cadastro_base','obs_executora_cadastro_base','capacitacao',
              'area_responsavel_capacitacao','atendimento','carga_horaria','cronograma','obs_risco','adequacao'
              ,'responsavel','obs_solicitante_cadastro_clientes']

    success_url = reverse_lazy('index')






class DeletePda(DeleteView):
    model = plano
    abstract = True

    template_name = 'Atendimento/templates/deletado.html'
    success_url = reverse_lazy('index')


    

def desativar(request, pk):
    template = loader.get_template('Atendimento/templates/desativado.html')
    pda = plano.objects.filter(id=pk)
    pda = pda[0]
    context = {
        'sistema': pda.sistema,
        'inquilino': pda.inquilino,
        
        }
    if (request.method == 'POST'):
        plano.objects.filter(id=pk).update(status = '4')
        print('Desativado')
        reverse_lazy('index')
        messages.info(request, 'Plano desativado com sucesso!')    
    else:
        print('Não desativado')

    

    return HttpResponse(template.render( context,request))



'''def Mudando(request, pk):
    template = loader.get_template('Atendimento/templates/desativado.html')
    context = {
        'sistema': plano.sistema,
        'inquilino': plano.inquilino,
        'desc_produto': plano.desc_produto,
        
        
        }
    
    plano.objects.filter(id=pk).update(status = '4')
    print('Desativado')
   

    return HttpResponse(template.render( context,request))'''



#plano.objects.filter(id=pk).update(status = '4')


    
    
  


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


    document = Document()

    document.add_heading('Proposta de Atendimento', 0)
    document.add_paragraph(pda_ed.sistema)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=proposta.docx'
    document.save(response)
    return response







