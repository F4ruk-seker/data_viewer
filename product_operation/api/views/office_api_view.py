from product_operation.api.serializers import OfficeSerializer
from product_operation.api.pegination import OfficePagination
from product_operation.models import Office
from rest_framework import filters
from rest_framework.generics import ListAPIView


class OfficeListView(ListAPIView):
    serializer_class = OfficeSerializer
    # pagination_class = OfficePagination
    filter_backends = [filters.SearchFilter]
    queryset = Office.objects.all().order_by("name")
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = 'name'

