from django.urls import path

from app_dnk.views import GeneticTestsListView


urlpatterns = [
    path("", GeneticTestsListView.as_view(), name="genetic_test"),
]
