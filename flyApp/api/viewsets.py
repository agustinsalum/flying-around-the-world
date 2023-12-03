from rest_framework.viewsets import ModelViewSet
from .models import Trip
from .serializers import VinoSerializer

class FlyViewSet(ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = VinoSerializer