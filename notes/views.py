from django.shortcuts import render

# Add in generic views for simplicity
from django.views.generic import ListView, DetailView

# Import our model
from .models import Note

class NoteListView(ListView):
    model = Note
    template_name = "note_list.html"


class NoteDetailView(DetailView):
    model = Note
    template_name = "note_detail.html"
