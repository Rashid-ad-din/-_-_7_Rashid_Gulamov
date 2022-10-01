from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from webapp.forms import SearchForm, NoteForm
from webapp.models import Note, StatusChoices


def add_view(request: WSGIRequest):
    note_form = NoteForm(request.POST)
    if not note_form.is_valid():
        return render(request, 'main.html', context={'form': note_form})
    note = Note.objects.create(**note_form.cleaned_data)
    return redirect('main')


def main_view(request: WSGIRequest):
    search_form = SearchForm
    note_form = NoteForm
    notes = Note.objects.exclude(status=StatusChoices.BLOCKED).order_by('-created_at')
    context = {
        'notes': notes,
        'search_form': search_form,
        'note_form': note_form
    }
    return render(request, 'main.html', context)


def search_view(request: WSGIRequest):
    search_form = SearchForm
    note_form = NoteForm
    search = request.GET.get('search')
    notes = Note.objects.filter(author__icontains=search).exclude(status=StatusChoices.BLOCKED).order_by('-created_at')
    context = {
        'notes': notes,
        'search_form': search_form,
        'note_form': note_form
    }
    return render(request, 'main.html', context)
