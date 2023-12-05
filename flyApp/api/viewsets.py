from rest_framework.viewsets import ModelViewSet
from ..models import Trip
from .serializers import TripSerializer

class FlyViewSet(ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer