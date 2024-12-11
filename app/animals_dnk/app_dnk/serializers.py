from rest_framework import serializers
import django_filters

from app_dnk.models import GeneticTests


class GeneticTestsSerializer(serializers.ModelSerializer):
    animal_name = django_filters.CharFilter(lookup_expr="icontains")
    species = django_filters.CharFilter(lookup_expr="icontains")
    test_date = django_filters.DateTimeFilter()
    milk_yield = django_filters.NumberFilter()
    health_status = django_filters.CharFilter(lookup_expr="icontains")
    created_at = django_filters.DateTimeFilter()

    class Meta:
        model = GeneticTests
        fields = "__all__"


class GeneticTestsListSerializer(serializers.ListSerializer):
    # Указываем, какой сериализатор использовать для элементов списка
    child = GeneticTestsSerializer()
