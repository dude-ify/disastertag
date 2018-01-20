from rest_framework import serializers
from .models import Dtag

class DtagSerializer(serializers.ModelSerializer):
    """Serializer to map Model instance into JSON format"""

    class Meta:
        """Meta class to map serializer's fields with the model fields"""
        model = Dtag
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
