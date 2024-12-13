from rest_framework import serializers

from app_dnk.models import GeneticTests


class GeneticTestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeneticTests
        fields = "__all__"


class GeneticTestsListSerializer(serializers.ListSerializer):
    # Указываем, какой сериализатор использовать для элементов списка
    child = GeneticTestsSerializer()



class StatisticSerializer(serializers.Serializer):
    species = serializers.CharField()
    total_tests = serializers.IntegerField()
    avg_milk_yield = serializers.FloatField()
    max_milk_yield = serializers.FloatField()
    good_health_percentage = serializers.FloatField()

class StatisticListSerializer(serializers.ListSerializer):
    child = StatisticSerializer()

