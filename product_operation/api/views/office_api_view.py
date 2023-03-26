from rest_framework.generics import ListAPIView
from product_operation.api.serializers import OfficeSerializer
from product_operation.models import Office
from product_operation.api.pegination import OfficePagination


class OfficeListView(ListAPIView):
    serializer_class = OfficeSerializer
    queryset = Office.objects.all()
    pagination_class = OfficePagination
    # def get_queryset(self):
    #     return super().get_queryset()