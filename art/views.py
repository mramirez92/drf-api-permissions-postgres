from .models import Art
from rest_framework import generics
from .serializers import ArtSerializer


class ArtList(generics.ListCreateAPIView):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer

class ArtDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer
