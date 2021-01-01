from django.urls import path

from notes.views import NoteListView, NoteDetailView

urlpatterns = [
    path('', NoteListView.as_view()),
    path('<int:pk>/', NoteDetailView.as_view()),
]
