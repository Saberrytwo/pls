from django.urls import path
from .views import indexPageView, drugPageView, prescriberPageView

urlpatterns = [
    path("", indexPageView, name='index'),
    path("drug/", drugPageView, name='drug'),
    path("prescriber/",prescriberPageView, name='prescriber' ),
]
