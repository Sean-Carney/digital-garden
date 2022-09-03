from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Note

admin.site.register(Note, MarkdownxModelAdmin)
