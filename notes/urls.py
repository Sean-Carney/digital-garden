from django.urls import path

from .views import NoteListView, NoteDetailView

urlpatterns = [
	path("<slug:slug>/", NoteDetailView.as_view(), name="note_detail"),
	path("", NoteListView.as_view(), name="note_list"),
]
