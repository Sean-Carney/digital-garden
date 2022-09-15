from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Note, NoteLink

admin.site.register(Note, MarkdownxModelAdmin)
