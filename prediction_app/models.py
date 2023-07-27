from django.db import models
from django.urls import reverse


class MoleculeSubmit(models.Model):

    smiles_string = models.CharField(
        max_length=256,
        help_text='Simple Molecular Input Line Entry System (SMILES) string'
    )

    class Meta:
        ordering = ['-smiles_string']

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.smiles_string
