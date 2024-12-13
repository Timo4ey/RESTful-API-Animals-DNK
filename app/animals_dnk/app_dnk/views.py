from typing import Any
from django.db.models.manager import BaseManager
from django.db.models import Count, Avg, Max, Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from drf_yasg.utils import swagger_auto_schema

from app_dnk.filters import GeneticTestsFilter
from app_dnk.models import GeneticTests
from app_dnk.serializers import GeneticTestsListSerializer, GeneticTestsSerializer, StatisticListSerializer
# Create your views here.


class GeneticTestsListView(APIView):
    model = GeneticTests

    @swagger_auto_schema(responses={200: GeneticTestsListSerializer})
    def get(self, request: Request) -> Response:
        queryset: BaseManager[GeneticTests] = GeneticTests.objects.all()
        filter_set = GeneticTestsFilter(request.GET, queryset=queryset)
        if filter_set.is_valid():

            serializer = GeneticTestsSerializer(filter_set.qs, many=True)

            return Response(serializer.data)
        return Response({"error": "Invalid filters", "details": filter_set.errors}, status=400)

    @swagger_auto_schema(
        request_body=GeneticTestsSerializer, responses={
            200: GeneticTestsSerializer}
    )
    def post(self, request):
        new_data = GeneticTestsSerializer(data=request.data)
        if new_data.is_valid():
            obj = new_data.save()
            return Response(
                status=201, data={"message": "Данные успешно добавлены", "id": obj.id}
            )
        return Response({"error": "Bad request", "details": new_data.errors}, status=400)


class StatisticsView(APIView):
    model = GeneticTests

    http_method_names = ['get']

    @swagger_auto_schema(
        responses={
            200: StatisticListSerializer}
    )
    def get(self, request: Request) -> Response:
        statistics = GeneticTests.objects.values('species').annotate(
            total_tests=Count("id"),
            avg_milk_yield=Avg("milk_yield"),
            max_milk_yield=Max("milk_yield"),
            good_health_percentage=(Count('id', filter=Q(
                health_status='good')) * 100.0 / Count("id"))
        )

        for stat in statistics:
            stat['avg_milk_yield'] = round(stat['avg_milk_yield'], 1)
            stat['good_health_percentage'] = round(
                stat['good_health_percentage'], 1)

        return Response(data=statistics, status=200)
