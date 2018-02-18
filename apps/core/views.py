
from django.shortcuts import render
from django.http.response import HttpResponse


def home(request):
    context = {}
    return render(request, 'core/home.html', context)
