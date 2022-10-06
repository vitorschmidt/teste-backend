from archive.serializers import FileSerializer
from .models import Archive
from rest_framework import generics


class FileView(generics.ListCreateAPIView):
    queryset = Archive.objects.all()
    serializer_class = FileSerializer