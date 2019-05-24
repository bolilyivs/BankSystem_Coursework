import django_filters
from django.forms import *
from Structure.models import * 


class CreditFilter(django_filters.FilterSet):
    class Meta:
        model = Credit
        fields = {
            'client__last_name': ['exact'],
            'client__first_name': ['exact'],
            'client__second_name': ['exact'],
            'department': ['exact'],
            'employee': ['exact'],
            'credit_type': ['exact'],
            'status': ['exact'],
            'money': ['lt', 'gt'],  
            'reg_date': ['exact','lt', 'gt'],
            'end_date': ['lt', 'gt'],
        }

        filter_overrides = {
            models.DateField:{
                'filter_class': django_filters.DateFilter,
                'extra': lambda f: {
                    'widget': DateInput(attrs={'type':'date'})
                },
            }
        }