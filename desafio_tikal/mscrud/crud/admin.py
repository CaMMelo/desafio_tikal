from django.contrib import admin

from . import models

admin.site.register(models.Cliente)
admin.site.register(models.Telefone)
admin.site.register(models.Email)
