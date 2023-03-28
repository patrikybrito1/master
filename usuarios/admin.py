from django.contrib import admin

from usuarios.models import Usuario
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
@admin.register(Usuario)

class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('nome', 'email', 'senha')