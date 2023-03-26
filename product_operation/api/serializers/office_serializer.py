from rest_framework import serializers
from product_operation.models import Office
from .performance_serializer import PerformanceSerializer


class OfficeSerializer(serializers.ModelSerializer):
    performance = PerformanceSerializer()

    class Meta:
        model = Office
        fields = '__all__'

        