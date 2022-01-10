from django.shortcuts import render


def index(request):
    return render(request, 'app/index.html')


def beauty_treatments(request):
    return render(request, 'app/about.html')
