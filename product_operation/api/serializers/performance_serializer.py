from rest_framework import serializers
from product_operation.models import PerformanceMetric


class PerformanceSerializer(serializers.ModelSerializer):
    metric = serializers.SerializerMethodField()
    total_metric = serializers.SerializerMethodField()

    def get_metric(self, obj):
        metric_list = obj.get_metric_as_percentile_ord_isgyh()
        return metric_list

    def get_total_metric(self, obj):
        metric_list = obj.get_total_metric()
        return metric_list

    class Meta:
        model = PerformanceMetric
        # fields = '__all__'
        exclude = ('id',)

