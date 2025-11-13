from django.contrib import admin
from .models import Regra, Nucleo, ElementoFlexionado, Mapeamento

# Registra os 4 modelos
admin.site.register(Regra)
admin.site.register(Nucleo)
admin.site.register(ElementoFlexionado)


# Uma forma mais bonita de mostrar o Mapeamento no admin
@admin.register(Mapeamento)
class MapeamentoAdmin(admin.ModelAdmin):
    list_display = ('frase_exemplo', 'nucleo', 'elemento', 'regra')
    list_filter = ('regra', 'nucleo')


from django.contrib import admin

# Register your models here.
