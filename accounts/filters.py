import django_filters

from .models import *


#Class that will handle the filter
class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order

