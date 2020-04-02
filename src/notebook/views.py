from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Note

class NoteView(generic.ListView):
    model = Note
    template_name = "notes.html"
    context_object_name = "notes"
