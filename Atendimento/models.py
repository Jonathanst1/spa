from django.db import models
from datetime import datetime
# Create your models here.

class plano(models.Model):
    CHOICES = (
        ('Sim', 'Sim'),
        ('Nao', 'Nao'))

    CHOICES2 = [('1', 'Ativo'), ('2', 'Em Elaboracao'), ('3', 'Inativo'),('4', 'Desativado')]
    versao = models.CharField(max_length=5, blank=True)
    status = models.CharField(max_length=13, choices = CHOICES2, default='Ativo')
    responsavel = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True )
    sistema = models.CharField(max_length=100, blank=True)
    inquilino = models.CharField(max_length=100, blank=True)
    demanda = models.CharField(max_length=100, blank=True)
    sub_demanda = models.CharField(max_length=100, blank=True)
    desc_produto = models.TextField(blank=True,max_length=500)
    n_contrato = models.CharField(max_length=100, blank=True)
    aditivo = models.CharField(max_length=100, blank=True)
    ans = models.CharField(max_length=100, blank=True)
    necessidades = models.TextField(max_length=200, blank=True)
    requisitos_LDPA = models.TextField(max_length=200, blank=True)
    solucoes_impactadas = models.TextField(max_length=200, blank=True)
    anexo_contexto = models.FileField(upload_to='files', max_length=255, blank=True, default='Nenhum arquivo anexado')
    telas_sistema = models.FileField(upload_to='files', max_length=255, blank=True, default='Nenhum arquivo anexado')
    cronograma_implantacao = models.FileField(upload_to='files', max_length=255, blank=True, default='Nenhum arquivo anexado')
    canais = models.CharField(max_length=100, blank=True)
    n1 = models.CharField(max_length=100, blank=True)
    n2 = models.CharField(max_length=100, blank=True)
    area_solicitante_cliente = models.CharField(max_length=100, blank=True)
    obs_solicitante_cliente = models.TextField(blank=True,max_length=500)
    area_executora_cliente = models.CharField(max_length=20, blank=True)
    obs_executora_cliente = models.TextField(blank=True,max_length=500)
    area_solicitante_usuario = models.CharField(max_length=100, blank=True)
    obs_solicitante_usuario = models.TextField(blank=True,max_length=500)
    area_executora_usuario = models.CharField(max_length=100, blank=True)
    obs_executora_usuario = models.TextField(blank=True,max_length=500)
    area_solicitante_base = models.CharField(max_length=100, blank=True)
    publicacao_solicitante_base = models.DateField(blank=True, null=True)
    obs_solicitante_base = models.TextField(blank=True,max_length=500)
    area_executora_base = models.CharField(max_length=100, blank=True)
    publicacao_executora_base = models.DateField(blank=True, null=True)
    obs_executora_base = models.TextField(blank=True,max_length=500)
    area_solicitante_itens = models.CharField(max_length=100, blank=True)
    obs_solicitante_itens = models.TextField(blank=True,max_length=500)
    area_executora_itens = models.CharField(max_length=100, blank=True)
    obs_executora_itens = models.TextField(blank=True,max_length=500)
    area_solicitante_cadastro_clientes = models.CharField(max_length=100, blank=True)
    area_executora_cadastro_clientes = models.CharField(max_length=100, blank=True)
    obs_executora_cadastro_clientes = models.TextField(blank=True,max_length=500)
    obs_solicitante_cadastro_clientes = models.TextField(blank=True,max_length=500)
    area_solicitante_cadastro_base = models.CharField(max_length=100, blank=True)
    publicacao_solicitante_cadastro_base = models.DateField(blank=True, null=True)
    obs_solicitante_cadastro_base = models.TextField(blank=True,max_length=500)
    area_executora_cadastro_base = models.CharField(max_length=100, blank=True)
    publicacao_executora_cadastro_base = models.DateField(blank=True, null=True)
    obs_executora_cadastro_base = models.TextField(blank=True,max_length=500)
    area_responsavel_capacitacao = models.CharField(max_length=100, blank=True)
    atendimento = models.CharField(max_length=100, blank=True)
    carga_horaria = models.CharField(max_length=100, blank=True)
    cronograma = models.FileField(upload_to='files', max_length=255, blank=True, default='Nenhum arquivo anexado')
    obs_risco = models.TextField(blank=True,max_length=500)
    capacitacao = models.TextField(max_length=20,  choices=CHOICES, blank=True ,default="Nao")
    adequacao = models.TextField(max_length=20, choices=CHOICES, blank=True, default="Nao")









    def __str__(self):
        if not self.id:
            self.created = datetime.now()

        self.modified = datetime.now()
        return self.inquilino + '-' + self.sistema



'''CreateDate DATETIME
DEFAULT
CURRENT_TIMESTAMP,
ModifiedDate
DATETIME
DEFAULT
CURRENT_TIMESTAMP,
sistema
NVARCHAR(100),
inquilino
NVARCHAR(100),
demanda
NVARCHAR(100),
sub_demanda
NVARCHAR(100),
des_produto
NVARCHAR(255),
n_contrato
NVARCHAR(100),
aditivo
NVARCHAR(100),
ans
NVARCHAR(255),
necessidades
NVARCHAR(255),
requisitos_LDPA
NVARCHAR(255),
solucoes_impactadas
NVARCHAR(255),
canais
NVARCHAR(100),
n1
NVARCHAR(100),
n2
NVARCHAR(100),
adequacao
INT(2),
area_solicitante_cliente
NVARCHAR(100),
obs_solicitante_cliente
NVARCHAR(255),
area_executora_cliente
NVARCHAR(100),
obs_executora_cliente
NVARCHAR(255),
area_solicitante_usuario
NVARCHAR(100),
obs_solicitante_usuario
NVARCHAR(255),
area_executora_usuario
NVARCHAR(100),
obs_executora_usuario
NVARCHAR(255),
area_solicitante_base
NVARCHAR(100),
publicacao_solicitante_base
VARCHAR(11),
obs_solicitante_base
NVARCHAR(255),
area_executora_base
NVARCHAR(100),
publicacao_executora_base
VARCHAR(11),
obs_executora_base
NVARCHAR(100),
area_solicitante_itens
NVARCHAR(100),
obs_solicitante_itens
NVARCHAR(255),
area_executora_itens
NVARCHAR(100),
obs_executora_itens
NVARCHAR(255),
area_solicitante_cadastro_clientes
NVARCHAR(100),
area_executora_cadastro_clientes
NVARCHAR(100),
obs_executora_cadastro_clientes
NVARCHAR(255),
area_solicitante_cadastro_base
NVARCHAR(100),
publicacao_solicitante_cadastro_base
VARCHAR(11),
obs_solicitante_cadastro_base
NVARCHAR(255),
area_executora_cadastro_base
NVARCHAR(100),
publicacao_executora_cadastro_base
VARCHAR(11),
obs_executora_cadastro_base
NVARCHAR(255),
capacitacao
INT(2),
area_responsavel_capacitacao
NVARCHAR(100),
atendimento
NVARCHAR(100),
carga_horaria
NVARCHAR(100),
-- cronograma
NVARCHAR(100),
obs_risco
NVARCHAR(255)'''