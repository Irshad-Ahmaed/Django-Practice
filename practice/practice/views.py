from django.http import HttpResponse
from django.shortcuts import render, redirect


def home(request):
    return HttpResponse("Welcome, to Home Page")

def templateHome(request):
    return render(request, "index.html")