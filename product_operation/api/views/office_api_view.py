from product_operation.api.serializers import OfficeSerializer
from product_operation.api.pegination import OfficePagination
from product_operation.models import Office
from rest_framework import filters
from rest_framework.generics import ListAPIView


class OfficeListView(ListAPIView):
    serializer_class = OfficeSerializer
    queryset = Office.objects.all()
    pagination_class = OfficePagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    ordering_fields = ['name']

