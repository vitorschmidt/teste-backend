from django.shortcuts import render
from rest_framework import generics

from manage_files.serializers import FileContentSerializer
from utils.create_database import insert_table
from utils.read_cnba import read_text
from .models import Manage_file
# Create your views here.


class ViewContentFile(generics.ListAPIView):

    queryset = Manage_file.objects.all()
    serializer_class = FileContentSerializer
