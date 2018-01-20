from rest_framework import generics
from .serializers import DtagSerializer
from .models import Dtag

class CreateView(generics.ListCreateAPIView):
    """This class defines creation in the rest api"""
    queryset = Dtag.objects.all()
    serializer_class = DtagSerializer

    def preform_create(self, seralizer):
        """Save the post data when creating a new Dtag"""
        seralizer.save()
