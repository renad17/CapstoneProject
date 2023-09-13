from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse



# Create your views here.

def home_view(request : HttpRequest):

    return render(request, "main/index.html")


def about_view(request: HttpRequest):

    return render(request, "main/about.html")

def not_found_view(request: HttpRequest):

    return render(request, "main/about.html")


