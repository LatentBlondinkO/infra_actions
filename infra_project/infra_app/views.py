from django.shortcuts import render


def index(request):
    template = 'infra_app/index.html'
    return render(request, template)


def second_page(request):
    template = 'infra_app/second_page.html'
    return render(request, template)
