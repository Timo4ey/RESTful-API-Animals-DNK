from django.db.models.manager import BaseManager
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from drf_yasg.utils import swagger_auto_schema

from app_dnk.models import GeneticTests
from app_dnk.serializers import GeneticTestsListSerializer, GeneticTestsSerializer

# Create your views here.


class GeneticTestsListView(APIView):
    model = GeneticTests

    @swagger_auto_schema(responses={200: GeneticTestsListSerializer})
    def get(self, request: Request) -> Response:
        genetic_tests: BaseManager[GeneticTests] = GeneticTests.objects.all()
        serializer = GeneticTestsSerializer(genetic_tests, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=GeneticTestsSerializer, responses={200: GeneticTestsSerializer}
    )
    def post(self, request):
        new_data = GeneticTestsSerializer(data=request.data)
        if new_data.is_valid():
            obj = new_data.save()
            return Response(
                status=201, data={"message": "Данные успешно добавлены", "id": obj.id}
            )
        return Response(status=400)
