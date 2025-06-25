# Register your models here.
from django.contrib import admin

from .models import User  # Importe seu modelo User


# Registre o modelo User no painel administrativo
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'created_at')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'created_at')

    # Para adicionar mais funcionalidades personalizadas
    # def save_model(self, request, obj, form, change):
    #    # Lógica personalizada ao salvar um modelo
    #    super().save_model(request, obj, form, change)
