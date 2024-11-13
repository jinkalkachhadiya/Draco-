from django.urls import path
from .views import *

ulrpatterns = [
    path('home/',home_view, name='home_view'),
]

