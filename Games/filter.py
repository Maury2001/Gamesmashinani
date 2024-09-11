import django_filters


from .models import*

class TeamFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name='date_created', lookup_expr='gte ')
    class Meta:
        model = Team
        fields ='__all__'
        exclude = ['played','won','loss','agg','plusminus','f','points','f','draw']