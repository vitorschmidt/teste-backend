from rest_framework import serializers
from .models import Archive

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archive
        fields = "__all__"