from django.contrib import admin
from .models import Cliente
from .models import Categoria

admin.site.register(Cliente)
admin.site.register(Categoria)