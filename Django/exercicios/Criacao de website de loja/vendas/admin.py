from django.contrib import admin
from .models import Venda
from .models import Cobranca
from .models import Entrega

admin.site.register(Venda)
admin.site.register(Cobranca)
admin.site.register(Entrega)
