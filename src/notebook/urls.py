from django.urls import path

from . import views

urlpatterns = [
    path('', views.NoteView.as_view(), name='notes'),
    path('<tag>', views.NoteView.as_view(), name='tags'),
]
