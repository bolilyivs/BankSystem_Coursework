import django_filters
from django.forms import *
from Structure.models import * 


class ClientFilter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = {
            'first_name': ['exact'],
            'second_name': ['exact'],
            'last_name': ['exact'],
            'conviction': ['exact'],
            'work': ['exact'],
            'house': ['exact'],
            'profit': ['exact'],
        }

        filter_overrides = {
            models.DateField:{
                'filter_class': django_filters.DateFilter,
                'extra': lambda f: {
                    'widget': DateInput(attrs={'type':'date'})
                },
            }
        }