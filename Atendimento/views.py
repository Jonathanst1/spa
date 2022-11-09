from django.shortcuts import render
from django.views import generic
from .models import plano
from django.template import loader
from django.http import HttpResponse

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

class CreateView(generic.ListView):
    model = plano
    template_name = 'Atendimento/templates/criarPlano.html'
    def get_queryset(self):
        return plano.objects.order_by('-created')





def ver(request, pda_id):
    pda = plano.objects.filter(id=pda_id)
    pda = pda[0]
    template = loader.get_template('Atendimento/templates/pda.html')
    context = {
               'id': pda.id,
                'sistema': pda.sistema
               }
    return HttpResponse(template.render(context, request))




def editar(request, pk):
    pda_ed = plano.objects.filter(id=pk)
    pda_ed = pda_ed[0]
    context = {
        'id': pda_ed.id,
        'sistema': pda_ed.sistema
    }
    return render(request, 'Atendimento/templates/editar.html', context)