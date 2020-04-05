from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import Note, Tag


class NoteView(ListView):
    model = Note
    template_name = "notes.html"
    context_object_name = "notes"

    def get_queryset(self):
        if self.kwargs.get("tag"):
            self.tag = get_object_or_404(Tag, name=self.kwargs["tag"])
            return Tag.objects.get(name=self.tag).note_set.all()
        else:
            return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context


class CreateNoteView(CreateView):
    model = Note
    template_name = "note_form.html"
    fields = ["title", "text", "tags"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context
