from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Note, Tag


class NoteView(generic.ListView):

    model = Note
    template_name = "notes.html"
    context_object_name = "notes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context
