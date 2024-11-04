from django.contrib import admin
from .models import Venda
from .models import Reserva

admin.site.register(Venda)
admin.site.register(Reserva)