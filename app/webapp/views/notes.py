from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

def main_view(request: WSGIRequest):
    return render(request, 'main.html')