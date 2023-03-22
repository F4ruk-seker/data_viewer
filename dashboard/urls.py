from django.contrib import admin
from django.urls import path
from .views import *


name = "dashboard"
urlpatterns = [
    path('', MainPage.as_view()),

]
