import django_filters
from django.forms import *
from Structure.models import * 


class PaymentFilter(django_filters.FilterSet):
    class Meta:
        model = Payment
        fields = {
            'client__last_name': ['exact'],
            'client__first_name': ['exact'],
            'client__second_name': ['exact'],
            'department': ['exact'],
            'employee': ['exact'],
            'status': ['exact'],
            'money': ['lt', 'gt'],  
            'reg_date': ['lt', 'gt'],
        }

        filter_overrides = {
            models.DateField:{
                'filter_class': django_filters.DateFilter,
                'extra': lambda f: {
                    'widget': DateInput(attrs={'type':'date'})
                },
            }
        }