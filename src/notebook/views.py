from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from .models import Note, Tag


class NoteView(generic.ListView):
    model = Note
    template_name = "notes.html"
    context_object_name = "notes"

    def get_queryset(self):
        if self.kwargs["tag"]:
            self.tag = get_object_or_404(Tag, name=self.kwargs["tag"])
            return Tag.objects.get(name=self.tag).note_set.all()
        else:
            return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context
