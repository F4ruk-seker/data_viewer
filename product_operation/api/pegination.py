from rest_framework import pagination


class OfficePagination(pagination.PageNumberPagination):
    page_size = 10
    ordering_fields = ['name']

    class Meta:
        ordering = ['-id']