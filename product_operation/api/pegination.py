from rest_framework import pagination


class OfficePagination(pagination.PageNumberPagination):
    page_size = 10

