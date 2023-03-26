from django.urls import path
from django.shortcuts import HttpResponse

from .views import OfficeListView

name = "product_operation_api"

urlpatterns = [
    path('', OfficeListView.as_view()),

]
