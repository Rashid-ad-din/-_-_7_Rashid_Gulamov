from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.forms import SearchForm
from webapp.models import Note, StatusChoices


def main_view(request: WSGIRequest):
    search_form = SearchForm
    notes = Note.objects.exclude(status=StatusChoices.BLOCKED).order_by('-created_at')
    context = {
        'notes': notes,
        'search_form': search_form
    }
    return render(request, 'main.html', context)


def search_view(request: WSGIRequest):
    search_form = SearchForm
    search = request.GET.get('search')
    notes = Note.objects.filter(author__icontains=search).exclude(status=StatusChoices.BLOCKED).order_by('-created_at')
    context = {
        'notes': notes,
        'search_form': search_form
    }
    return render(request, 'main.html', context)
