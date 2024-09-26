from django.contrib import admin
from .models import Produto
from .models import Categoria
from .models import Grupo

admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Grupo)
