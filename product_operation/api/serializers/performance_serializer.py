from rest_framework import serializers
from product_operation.models import PerformanceMetric


class PerformanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = PerformanceMetric
        # fields = '__all__'
        exclude = ('id',)

