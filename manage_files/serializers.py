from rest_framework import serializers
from utils.create_database import insert_table

from utils.read_cnba import read_text
from .models import Manage_file

class FileContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manage_file
        fields = "__all__"
