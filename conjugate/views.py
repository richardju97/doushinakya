from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def hello(request):
    text = """<h1>Welcome to Doushinakya!</h1>"""
    return HttpResponse(text)
