from django.contrib import admin
from .models import Link
@admin.register(Link)
class Linkadmin(admin.ModelAdmin):
    readonly_fields = ('criado','alterado')
    list_display = ('chave','criado','alterado')

# Register your models here.
