from rest_framework.generics import ListAPIView, RetrieveAPIView

from notes.models import Note
from notes.serializers import NoteSerializer


class NoteListView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetailView(RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
