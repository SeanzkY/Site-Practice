from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "site.html")


def game(request):
    return render(request, 'ticTacToe.html')
