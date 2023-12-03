from rest_framework.serializers import ModelSerializer
from .models import Trip

class VinoSerializer(ModelSerializer):
    class Meta:
        model = Trip
        fields = "__all__"