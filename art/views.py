from .models import Art
from rest_framework import generics
from .serializers import ArtSerializer
from .permissions import IsOwnerOrReadOnly


class ArtList(generics.ListCreateAPIView):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer


class ArtDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly, )
    queryset = Art.objects.all()
    serializer_class = ArtSerializer
