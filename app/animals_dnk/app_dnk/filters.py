import django_filters

from app_dnk.models import GeneticTests


class GeneticTestsFilter(django_filters.FilterSet):
    animal_name = django_filters.CharFilter(lookup_expr="icontains")
    species = django_filters.CharFilter(lookup_expr="icontains")
    test_date = django_filters.DateTimeFilter()
    milk_yield = django_filters.NumberFilter()
    health_status = django_filters.CharFilter(lookup_expr="icontains")
    created_at = django_filters.DateTimeFilter()

    class Meta:
        model = GeneticTests
        fields = ["animal_name", "species", "test_date", "milk_yield", "health_status", "created_at"] 
