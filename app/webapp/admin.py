from django.contrib import admin

# Register your models here.
from webapp.models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'email', 'created_at', 'status')
    list_filter = ('id', 'author', 'status')
    search_fields = ('author', 'status')
    fields = ('author', 'email', 'text', 'created_at', 'changed_at', 'status')
    readonly_fields = ('id', 'created_at', 'changed_at')


admin.site.register(Note, NoteAdmin)
