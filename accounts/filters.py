import django_filters
from django_filters import DateFilter

from .models import *


#Class that will handle the filter
class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr='gte') #greaterthanorequal
    end_date = DateFilter(field_name="date_created", lookup_expr='lte') #lessthanorequal
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created'] #to exclude the Customer and Date Created field
    
