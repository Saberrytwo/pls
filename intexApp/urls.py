from django.urls import path
from .views import prescriberPageView, drugPageView

urlpatterns = [
    path("", prescriberPageView, name='prescriber'),
    path("drug/", drugPageView, name='drug')
]
