from django.contrib import admin
from .models import plano,Acesso

class planoStatus(admin.ModelAdmin):
    list_display = ['sistema','status']

# Register your models here.
admin.site.register(plano,planoStatus),
admin.site.register(Acesso)



# Register your models here.
