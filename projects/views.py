from django.shortcuts import render


PAGE_TITLE = 'CLINK | CAPITAL'


def index(request):
    template = 'index.html'
    context = {
        'title': PAGE_TITLE
    }
    return render(request, template, context)
