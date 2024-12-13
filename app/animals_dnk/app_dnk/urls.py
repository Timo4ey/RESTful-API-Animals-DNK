from django.urls import path

from app_dnk.views import GeneticTestsListView, StatisticsView


urlpatterns = [
    path("tests/", GeneticTestsListView.as_view(), name="genetic_test"),
    path("statistics/", StatisticsView.as_view(), name="statistics"),
]
