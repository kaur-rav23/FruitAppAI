from rest_framework import generics
from .models import FruitFAQ
from .serializers import FruitFAQSerializer

class FruitFAQListCreate(generics.ListCreateAPIView):
    queryset = FruitFAQ.objects.all()
    serializer_class = FruitFAQSerializer

class FruitFAQRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = FruitFAQ.objects.all()
    serializer_class = FruitFAQSerializer
