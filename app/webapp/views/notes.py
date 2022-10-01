from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

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


def edit_view(request: WSGIRequest, pk):
    note = get_object_or_404(Note, pk=pk)
    note_form = NoteForm(initial={
        'author': note.author,
        'email': note.email,
        'text': note.text,
    })
    if request.method == 'GET':
        return render(request, 'edit.html', context={'note': note, 'note_form': note_form})
    note_form = NoteForm(request.POST)
    if not note_form.is_valid():
        return render(request, 'edit.html', context={'note': note, 'note_form': note_form})
    note.author = note_form.cleaned_data['author']
    note.email = note_form.cleaned_data['email']
    note.text = note_form.cleaned_data['text']
    note.save()
    return redirect('main')


def delete_view(request: WSGIRequest, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'delete.html', context={'note': note})


def confirm_delete_view(request: WSGIRequest, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('main')
