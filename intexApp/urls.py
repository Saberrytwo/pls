from django.urls import path
from .views import indexPageView, drugPageView, prescriberPageView, searchDrugsPageView, searchPrescribersPageView

urlpatterns = [
    path("", indexPageView, name='index'),
    path("drug/", drugPageView, name='drug'),
    path("prescriber/",prescriberPageView, name='prescriber' ),
    path("searchDrugs", searchDrugsPageView, name='searchDrugs'),
    path("searchPrescribers/", searchPrescribersPageView, name='searchPrescribers'),
]
