import django_filters
from django_filters import DateFilter, CharFilter

from risks.models import Risk
from tasks.models import Task
from projects.models import Project
from custs.models import Customer

class RiskFilter(django_filters.FilterSet):
    description = CharFilter(field_name='description', lookup_expr='icontains')
    
    start_date = DateFilter(field_name="dateCreated", lookup_expr='gte')
    update_date = DateFilter(field_name="dateUpdated", lookup_expr='gte')
    end_date = DateFilter(field_name="dateFinished", lookup_expr='lte')

    
    class Meta: 
        model = Risk
        fields = '__all__'
        exclude = ['status', 'rrp', 'effect', 'dateCreated', 'dateUpdated'
        'dateFinished', 'description']
