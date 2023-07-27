from django.contrib import admin

from .models import MoleculeSubmit


class MoleculeSubmitAdmin(admin.ModelAdmin):
    pass


admin.site.register(MoleculeSubmit, MoleculeSubmitAdmin)
