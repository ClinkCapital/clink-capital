from django.http import HttpResponse, response
from django.shortcuts import render


PAGE_TITLE = 'Clink|Capital'


def index(request):
    template = 'index.html'
    context = {
        'title': PAGE_TITLE
    }
    return render(request, template, context)
