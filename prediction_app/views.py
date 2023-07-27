from django.shortcuts import render

from .models import MoleculeSubmit


def index(request):

    context = {
        'num_predictions': MoleculeSubmit.objects.all().count()
    }
    return render(request, 'index.html', context=context)
